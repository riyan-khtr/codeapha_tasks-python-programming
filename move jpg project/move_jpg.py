import os
import shutil

SOURCE_FOLDER = r"A:\Desktop\HTML files\Python\TestPhotos"
DEST_FOLDER = r"A:\Desktop\HTML files\Python\MovedJPG"

def move_jpg_files():
    # Create destination folder if it doesn't exist
    if not os.path.exists(DEST_FOLDER):
        os.makedirs(DEST_FOLDER)

    # Loop through files in source folder
    for file in os.listdir(SOURCE_FOLDER):
        if file.lower().endswith(".jpg"):
            src = os.path.join(SOURCE_FOLDER, file)
            dest = os.path.join(DEST_FOLDER, file)

            shutil.move(src, dest)
            print(f"Moved: {file}")

    print("\nAll JPG files moved successfully!")

if __name__ == "__main__":
    move_jpg_files()