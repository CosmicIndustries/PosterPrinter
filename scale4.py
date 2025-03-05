from PIL import Image
import fitz  # PyMuPDF
import os

# Disable decompression bomb check if needed (use with caution)
Image.MAX_IMAGE_PIXELS = None

def resize_image(image, target_width, target_height):
    """Resize the image to the specified target width and height."""
    return image.resize((target_width, target_height), Image.LANCZOS)

def apply_rotation(image, orientation_mode, angle=0):
    """
    Apply rotation based on the selected orientation mode.
    
    - 'portrait': No rotation.
    - 'landscape': Rotates 90 degrees.
    - 'arbitrary': Rotates by the specified angle.
    """
    if orientation_mode == "portrait":
        return image
    elif orientation_mode == "landscape":
        return image.rotate(90, expand=True)
    elif orientation_mode == "arbitrary":
        return image.rotate(angle, expand=True)
    else:
        print("Unknown orientation mode. Proceeding without rotation.")
        return image

def split_image(image_path, output_folder, rows, cols, tile_width, tile_height, overlap, orientation_mode, angle):
    """Split image into smaller tiles based on the specified grid and tile dimensions."""
    # Calculate overall target dimensions (entire image area)
    target_width = tile_width * cols
    target_height = tile_height * rows

    image = Image.open(image_path)
    # Apply rotation if needed
    image = apply_rotation(image, orientation_mode, angle)
    # Resize image to the overall intended dimensions
    image = resize_image(image, target_width, target_height)

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Split the resized image into tiles
    for row in range(rows):
        for col in range(cols):
            left = max(0, col * tile_width - overlap)
            upper = max(0, row * tile_height - overlap)
            right = min(target_width, left + tile_width + overlap)
            lower = min(target_height, upper + tile_height + overlap)

            tile = image.crop((left, upper, right, lower))
            tile.save(f"{output_folder}/tile_{row+1}_{col+1}.png")

    print(f"Image resized to {target_width}x{target_height} and split into {rows * cols} tiles with {overlap}px overlap saved to {output_folder}.")

def split_pdf(pdf_path, output_folder, rows, cols, tile_width, tile_height, dpi, overlap, orientation_mode, angle):
    """Split a PDF into images and then into smaller tiles based on the specified grid and tile dimensions."""
    target_width = tile_width * cols
    target_height = tile_height * rows

    doc = fitz.open(pdf_path)

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for page_num in range(len(doc)):
        page = doc[page_num]
        pix = page.get_pixmap(dpi=dpi)
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        # Apply rotation to the page image if needed
        img = apply_rotation(img, orientation_mode, angle)
        # Resize the rotated image to the overall intended dimensions
        img = resize_image(img, target_width, target_height)

        img_path = f"{output_folder}/page_{page_num+1}.png"
        img.save(img_path, dpi=(dpi, dpi))

        # For splitting into tiles, use a standard 'portrait' orientation
        split_image(img_path, output_folder, rows, cols, tile_width, tile_height, overlap, "portrait", 0)

    print(f"PDF resized to {target_width}x{target_height} and split into {rows * cols} tiles per page with {overlap}px overlap saved to {output_folder}.")

def get_paper_size_dimensions(paper_size, dpi):
    """Return the tile dimensions (width and height in pixels) based on the selected paper size and DPI."""
    paper_sizes_in_inches = {
        "letter": (8.5, 11),
        "a4": (8.3, 11.7),
        "legal": (8.5, 14),
    }
    width_in_inches, height_in_inches = paper_sizes_in_inches.get(paper_size.lower(), paper_sizes_in_inches["letter"])
    width_in_pixels = int(width_in_inches * dpi)
    height_in_pixels = int(height_in_inches * dpi)
    return width_in_pixels, height_in_pixels

if __name__ == "__main__":
    file_path = input("Enter the file path (image or PDF): ")
    output_folder = input("Enter the output folder: ")

    try:
        rows = int(input("Enter the number of rows: "))
        cols = int(input("Enter the number of columns: "))
        dpi = int(input("Enter the DPI (e.g., 900): "))
        overlap = int(input("Enter the overlap in pixels (default 0): "))
        paper_size = input("Enter the paper size (letter, a4, legal): ").lower()
        orientation_mode = input("Enter the orientation mode (portrait, landscape, arbitrary): ").lower()
        angle = 0
        if orientation_mode == "arbitrary":
            angle = float(input("Enter the rotation angle in degrees: "))
    except ValueError:
        print("Error: Please enter valid numeric values for rows, columns, DPI, overlap, and angle.")
        exit(1)

    # Get the tile dimensions for the chosen paper size and DPI
    tile_width, tile_height = get_paper_size_dimensions(paper_size, dpi)
    print(f"Each tile will be {tile_width}x{tile_height} pixels.")

    if file_path.lower().endswith(".pdf"):
        split_pdf(file_path, output_folder, rows, cols, tile_width, tile_height, dpi, overlap, orientation_mode, angle)
    else:
        split_image(file_path, output_folder, rows, cols, tile_width, tile_height, overlap, orientation_mode, angle)
