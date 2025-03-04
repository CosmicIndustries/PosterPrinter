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
#**Poster Creator** 
script (for splitting and printing high-resolution posters):

---

### High-Resolution Poster Creator

A Python script that allows you to **split high-resolution images** or **PDFs into smaller tiles** for printing large posters on multiple sheets of paper. The script supports splitting images or PDF pages into smaller tiles with optional overlap, ensuring precise alignment when piecing together printed pages. Ideal for creating large posters, wall art, or any high-quality print jobs.

---

### Features:
- Split large images or PDF pages into smaller tiles for printing.
- Supports **overlap** between tiles to ensure precise alignment.
- **Resize** images or PDFs to the desired resolution for optimal print quality.
- Works with both **images** and **PDFs**, converting PDF pages to images before splitting.
- Adjustable number of rows, columns, and target print size.

---

### Requirements:
- **Python 3.x**
- **Pillow** (for image processing)
- **PyMuPDF (fitz)** (for working with PDFs)

To install the required dependencies:
```bash
pip install Pillow PyMuPDF
```

---

### Usage:
1. Clone or download the repository.
2. Run the `poster_creator.py` script.
3. Enter the file path (image or PDF), the target width and height for the tiles, the number of rows and columns, DPI, and overlap settings.
4. The script will output each tile as a separate image file, ready for printing.

---

### Example:
```bash
python poster_creator.py
```
You will be prompted to enter:
- The file path of the image or PDF.
- The number of rows and columns for the poster tiles.
- The target width and height of each tile.
- DPI (for high-quality printing).
- Overlap for tile alignment.

---

### Notes:
- Make sure your printer can handle the tile sizes and has adequate resolution to print large posters.
- The script will generate individual tile images, which you can print and assemble into a larger poster.
- Use this script with images or PDFs that need to be printed at high quality, such as artwork, large maps, or any oversized images.

---

### License:
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


