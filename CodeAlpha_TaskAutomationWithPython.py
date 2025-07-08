import os
import shutil

def move_jpg_files(src_dir, dest_dir):
    # Create destination folder if it doesn't exist
    os.makedirs(dest_dir, exist_ok=True)
    
    # Iterate over items in source directory
    for filename in os.listdir(src_dir):
        # Check for .jpg extension (case-insensitive)
        if filename.lower().endswith('.jpg'):
            src_path = os.path.join(src_dir, filename)
            dest_path = os.path.join(dest_dir, filename)
            shutil.move(src_path, dest_path)
            print(f'Moved: {filename}')

if __name__ == '__main__':
    # Replace these with your actual paths
    source = 'path/to/source_folder'
    destination = 'path/to/destination_folder'
    move_jpg_files(source, destination)