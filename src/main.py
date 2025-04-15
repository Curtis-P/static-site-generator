
import sys
import shutil
import os
from markdown_to_html import markdown_to_html_node

def main():
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"
    clear_dir("docs")
    copy_dir("static", "docs")
    generate_pages_recursively('content', 'template.html', 'docs', basepath)


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


def extract_title(markdown):
    blocks = markdown.split("\n\n")
    for block in blocks:
        if block.startswith("# "):
            return block[2:].strip()
        
    raise Exception("No H1 Title in document")

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as content_fs:
        new_content = content_fs.read()
    with open(template_path) as template_fs:
        template_content = template_fs.read()
    title = extract_title(new_content)
    new_content = markdown_to_html_node(new_content).to_html()
    
    templated_content = template_content.replace("{{ Title }}", title)   
    templated_content = templated_content.replace("{{ Content }}", new_content)   
    templated_content = templated_content.replace('href="/', f'href="{basepath}')   
    templated_content = templated_content.replace('src="/', f'src="{basepath}')   

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, 'w') as dest_fs:
         dest_fs.write(templated_content)

def generate_pages_recursively(dir_path_content, template_path, dest_dir_path, basepath):
    print(f"***    Generating page from {dir_path_content} to {dest_dir_path} using {template_path}    ***")
    file_structure = os.listdir(dir_path_content)
    for fs_object in file_structure:
        current_path = os.path.join(dir_path_content, fs_object)
        if os.path.isfile(current_path) and current_path.endswith(".md"):
            dest_file_path = os.path.join(dest_dir_path, fs_object.replace('.md','.html'))
            generate_page(current_path,template_path,dest_file_path, basepath)
        elif os.path.isdir(current_path):
            sub_dest_dir_path = os.path.join(dest_dir_path, fs_object)
            os.makedirs(sub_dest_dir_path, exist_ok=True)
            generate_pages_recursively(current_path, template_path, sub_dest_dir_path, basepath)
    
    
    

if __name__ == "__main__":
    main()