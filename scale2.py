from PIL import Image
import fitz  # PyMuPDF
import os

# Disable decompression bomb check if needed (use with caution)
Image.MAX_IMAGE_PIXELS = None

def resize_image(image, target_width, target_height):
    return image.resize((target_width, target_height), Image.LANCZOS)

def split_image(image_path, output_folder, rows, cols, tile_width, tile_height, overlap):
    # Calculate overall dimensions based on tile dimensions and grid layout
    target_width = tile_width * cols
    target_height = tile_height * rows
    
    image = Image.open(image_path)
    image = resize_image(image, target_width, target_height)
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for row in range(rows):
        for col in range(cols):
            # Compute tile boundaries with overlap
            left = max(0, col * tile_width - overlap)
            upper = max(0, row * tile_height - overlap)
            right = min(target_width, left + tile_width + overlap)
            lower = min(target_height, upper + tile_height + overlap)
            
            tile = image.crop((left, upper, right, lower))
            tile.save(f"{output_folder}/tile_{row+1}_{col+1}.png")
    
    print(f"Image resized to {target_width}x{target_height} and split into {rows * cols} tiles with {overlap}px overlap saved to {output_folder}.")

def split_pdf(pdf_path, output_folder, rows, cols, tile_width, tile_height, dpi, overlap):
    # Calculate overall dimensions based on tile dimensions and grid layout
    target_width = tile_width * cols
    target_height = tile_height * rows
    
    doc = fitz.open(pdf_path)
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for page_num in range(len(doc)):
        page = doc[page_num]
        pix = page.get_pixmap(dpi=dpi)
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        img = resize_image(img, target_width, target_height)
        img_path = f"{output_folder}/page_{page_num+1}.png"
        img.save(img_path, dpi=(dpi, dpi))
        
        split_image(img_path, output_folder, rows, cols, tile_width, tile_height, overlap)
    
    print(f"PDF resized to {target_width}x{target_height} and split into {rows * cols} tiles per page with {overlap}px overlap saved to {output_folder}.")

if __name__ == "__main__":
    file_path = input("Enter the file path (image or PDF): ")
    output_folder = input("Enter the output folder: ")
    
    try:
        rows = int(input("Enter the number of rows: "))
        cols = int(input("Enter the number of columns: "))
        dpi = int(input("Enter the DPI (e.g., 900): "))
        overlap = int(input("Enter the overlap in pixels (default 0): "))
    except ValueError:
        print("Error: Please enter valid numeric values.")
        exit(1)
    
    # Calculate tile dimensions based on 8.5x11 inches at the specified DPI
    tile_width = int(8.5 * dpi)
    tile_height = int(11 * dpi)
    
    print(f"Each tile will be {tile_width}x{tile_height} pixels.")
    
    if file_path.lower().endswith(".pdf"):
        split_pdf(file_path, output_folder, rows, cols, tile_width, tile_height, dpi, overlap)
    else:
        split_image(file_path, output_folder, rows, cols, tile_width, tile_height, overlap)
