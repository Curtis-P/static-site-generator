

import shutil
import os

def main():
    
    clear_dir("public")
    copy_dir("static", "public")


def clear_dir(dest_dir):
    if os.path.exists(dest_dir):
        shutil.rmtree(dest_dir)
    os.mkdir(dest_dir)
    
def copy_dir(src_path, dest_path):
    if not os.path.exists(dest_path):
        os.mkdir(dest_path)
    items = os.listdir(src_path)

    for item in items:
        src_item_path = os.path.join(src_path, item)
        dest_item_path = os.path.join(dest_path, item)
        if os.path.isfile(src_item_path):
            print(f"Copying file: {src_item_path} to {dest_item_path}")
            shutil.copy(src_item_path, dest_item_path)
        elif os.path.isdir(src_item_path):
            print(f"Copying Directory: {src_item_path}")
            copy_dir(src_item_path, dest_item_path)
            
if __name__ == "__main__":
    main()