#  Move JPG Files Automation Script

##  Overview
This Python script automates the task of organizing image files by moving all `.jpg` files from one folder to another. It helps reduce manual effort and keeps image folders neatly arranged.

##  Objective
To automatically detect JPG files in a source directory and move them into a destination directory using Python.

##  Technologies & Concepts Used
- Python
- os module (file and path handling)
- shutil module (moving files)
- File system automation

## Project Files
- `move_jpg.py` – Python script to move JPG files

##  How to Run
1. Open `move_jpg.py` and set:
   ```python
   SOURCE_FOLDER = r"your_source_path"
   DEST_FOLDER = r"your_destination_path"