import os
import sys
import time
import subprocess

def batch_print(folder_path, delay=5):
    # List files in the directory and filter for image files (modify as needed)
    for filename in os.listdir(folder_path):
        if filename.lower().endswith((".png", ".jpg", ".jpeg", ".pdf")):
            filepath = os.path.join(folder_path, filename)
            print(f"Sending {filepath} to the printer...")
            
            if sys.platform.startswith('win'):
                # On Windows, use os.startfile with the "print" command.
                try:
                    os.startfile(filepath, "print")
                except Exception as e:
                    print(f"Error printing {filepath}: {e}")
            elif sys.platform.startswith('darwin'):
                # On macOS, use the lp command.
                subprocess.run(["lp", filepath])
            else:
                # On Linux, use the lpr command.
                subprocess.run(["lpr", filepath])
            
            # Pause to avoid overloading the printer queue.
            time.sleep(delay)

if __name__ == "__main__":
    folder_path = input("Enter the folder path containing the files to print: ").strip()
    
    if not os.path.isdir(folder_path):
        print("The provided folder path does not exist.")
    else:
        batch_print(folder_path)
        print("Batch printing completed.")
