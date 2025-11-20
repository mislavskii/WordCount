import os
import shutil
import sys
from pathlib import Path

def organize_files(directory_path):
    """
    Organizes files in the specified directory by moving .jpg files to 'in' folder
    and .docx files to 'out' folder.
    
    Args:
        directory_path (str): Path to the directory to organize
    """
    # Convert to Path object for easier handling
    directory = Path(directory_path)
    
    # Check if directory exists
    if not directory.exists():
        print(f"Error: Directory '{directory_path}' does not exist.")
        return False
    
    if not directory.is_dir():
        print(f"Error: '{directory_path}' is not a directory.")
        return False
    
    # Create 'in' and 'out' folders if they don't exist
    in_folder = directory / "in"
    out_folder = directory / "out"
    
    try:
        in_folder.mkdir(exist_ok=True)
        out_folder.mkdir(exist_ok=True)
        print(f"Created folders: '{in_folder}' and '{out_folder}'")
    except Exception as e:
        print(f"Error creating folders: {e}")
        return False
    
    # Move .jpg files to 'in' folder
    jpg_files_moved = 0
    for file_path in directory.glob("*.jpg"):
        if file_path.is_file():
            try:
                destination = in_folder / file_path.name
                shutil.move(str(file_path), str(destination))
                print(f"Moved '{file_path.name}' to '{in_folder}'")
                jpg_files_moved += 1
            except Exception as e:
                print(f"Error moving file '{file_path.name}': {e}")
    
    # Move .docx files to 'out' folder
    docx_files_moved = 0
    for file_path in directory.glob("*.docx"):
        if file_path.is_file():
            try:
                destination = out_folder / file_path.name
                shutil.move(str(file_path), str(destination))
                print(f"Moved '{file_path.name}' to '{out_folder}'")
                docx_files_moved += 1
            except Exception as e:
                print(f"Error moving file '{file_path.name}': {e}")
    
    print(f"\nOrganization complete!")
    print(f"Moved {jpg_files_moved} .jpg files to '{in_folder}'")
    print(f"Moved {docx_files_moved} .docx files to '{out_folder}'")
    return True

def main():
    """Main function to run the file organizer"""
    if len(sys.argv) != 2:
        print("Usage: python file_organizer.py <directory_path>")
        print("Example: python file_organizer.py /path/to/your/folder")
        return
    
    directory_path = sys.argv[1]
    print(f"Organizing files in: {directory_path}")
    
    if organize_files(directory_path):
        print("\nFile organization completed successfully!")
    else:
        print("\nFile organization failed!")
        sys.exit(1)

if __name__ == "__main__":
    main()