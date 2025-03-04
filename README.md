# PosterPrinter
  Print images as Posters

---

### Batch Image Printer for Windows

A simple Python script to **batch print image files** from a specified folder using the default printer on Windows. The script supports common image formats (e.g., `.png`, `.jpg`, `.jpeg`, `.bmp`, `.gif`) and sends each image to the printer one by one. It uses the **PyWin32** library to interface with the Windows printing system.

---

### Features:
- Batch print all images in a folder.
- Automatically detects the default printer.
- Supports multiple common image formats (PNG, JPG, JPEG, BMP, GIF).
- Easy-to-use input interface for specifying the folder path.
- Prints images at their original resolution.

---

### Requirements:
- **Python 3.x**
- **Pillow** (for image handling)
- **PyWin32** (for Windows printing support)

To install the required dependencies:
```bash
pip install Pillow pywin32
```

---

### Usage:
1. Clone or download the repository.
2. Run the `batch_print.py` script.
3. Enter the full folder path containing your images when prompted.
4. The script will send each image in the folder to the default printer.

---

### Example:
```bash
python batch_print.py
```
You will be prompted to enter the path to the folder containing images to print.

---

### Notes:
- Make sure your printer is configured and ready.
- This script prints images at their native resolution and might require sufficient system resources for large images.
- You can easily adjust the script to add more print settings or customizations as needed.

---

### License:
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to adjust any of the content based on specific details you'd like to highlight. Would you like help setting up the repository itself as well?
