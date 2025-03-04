import os
import win32print
import win32ui
from PIL import Image, ImageWin

def print_image_win32(image_path):
    """Function to send a single image to the default printer"""
    printer_name = win32print.GetDefaultPrinter()  # Get the default printer
    hDC = win32ui.CreateDC()  # Create a device context
    hDC.CreatePrinterDC(printer_name)  # Initialize printer device context
    
    img = Image.open(image_path)  # Open the image
    dib = ImageWin.Dib(img)  # Convert the image to a DIB format
    
    # Start the print job and send the image to the printer
    hDC.StartDoc(os.path.basename(image_path))  # Start a new document
    hDC.StartPage()  # Start a new page
    
    # Draw the image on the printer device context
    dib.draw(hDC.GetHandleOutput(), (0, 0, img.width, img.height))
    
    hDC.EndPage()  # End the page
    hDC.EndDoc()  # End the document
    hDC.DeleteDC()  # Clean up the device context

    print(f"Successfully printed: {image_path}")

def batch_print_images(folder_path):
    """Function to print all image files in the given folder"""
    # Check if the folder exists
    if not os.path.isdir(folder_path):
        print(f"Error: The folder '{folder_path}' does not exist.")
        return
    
    # List all files in the folder and filter for image files
    image_files = [f for f in os.listdir(folder_path) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif'))]
    
    if not image_files:
        print(f"No image files found in the folder: {folder_path}")
        return
    
    # Iterate over each image file and print it
    for image_file in image_files:
        image_path = os.path.join(folder_path, image_file)
        print_image_win32(image_path)  # Print the image
    
    print("Batch printing completed.")

if __name__ == "__main__":
    # Input the folder path
    folder_path = input("Enter the folder path containing the images to print: ").strip()
    
    # Perform batch printing of images in the folder
    batch_print_images(folder_path)
