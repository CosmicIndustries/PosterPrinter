from PIL import Image
Image.MAX_IMAGE_PIXELS = None  # or set to a higher integer value
import fitz  # PyMuPDF
import os

def resize_image(image, target_width, target_height, dpi=300):
    return image.resize((target_width, target_height), Image.LANCZOS)

def split_image(image_path, output_folder, rows, cols, target_width, target_height, overlap):
    image = Image.open(image_path)
    image = resize_image(image, target_width, target_height)
    
    tile_w = target_width // cols
    tile_h = target_height // rows
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for row in range(rows):
        for col in range(cols):
            left = max(0, col * tile_w - overlap)
            upper = max(0, row * tile_h - overlap)
            right = min(target_width, left + tile_w + overlap)
            lower = min(target_height, upper + tile_h + overlap)
            
            tile = image.crop((left, upper, right, lower))
            tile.save(f"{output_folder}/tile_{row+1}_{col+1}.png")
    
    print(f"Image resized and split into {rows * cols} tiles with {overlap}px overlap and saved to {output_folder}.")

def split_pdf(pdf_path, output_folder, rows, cols, target_width, target_height, dpi, overlap):
    doc = fitz.open(pdf_path)
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for page_num in range(len(doc)):
        page = doc[page_num]
        pix = page.get_pixmap()
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        img = resize_image(img, target_width, target_height, dpi)
        img_path = f"{output_folder}/page_{page_num+1}.png"
        img.save(img_path, dpi=(dpi, dpi))
        
        split_image(img_path, output_folder, rows, cols, target_width, target_height, overlap)
    
    print(f"PDF resized and split into {rows * cols} pages per sheet with {overlap}px overlap and saved to {output_folder}.")

if __name__ == "__main__":
    file_path = input("Enter the file path (image or PDF): ")
    output_folder = input("Enter the output folder: ")
    
    try:
        rows = int(input("Enter the number of rows: "))
        cols = int(input("Enter the number of columns: "))
        target_width = int(input("Enter the target width in pixels: "))
        target_height = int(input("Enter the target height in pixels: "))
        dpi = int(input("Enter the DPI (default 300): "))
        overlap = int(input("Enter the overlap in pixels (default 0): "))
    except ValueError:
        print("Error: Please enter valid numeric values for rows, columns, dimensions, DPI, and overlap.")
        exit(1)
    
    if file_path.lower().endswith(".pdf"):
        split_pdf(file_path, output_folder, rows, cols, target_width, target_height, dpi, overlap)
    else:
        split_image(file_path, output_folder, rows, cols, target_width, target_height, overlap)
