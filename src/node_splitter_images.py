from textnode import TextNode, TextType
from image_extractor import extract_markdown_images

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        images = extract_markdown_images(node.text)
        if not images:
            new_nodes.append(node)
            continue
        results = []
        current_text = node.text
        for alt, url in images:
            full_img = f"![{alt}]({url})"
            parts = current_text.split(full_img)
            if parts[0]:
                results.append(TextNode(parts[0], TextType.TEXT))
            results.append(TextNode(alt, TextType.IMAGE, url))
            if len(parts) > 1:
                current_text = parts[1]
            else:
                current_text = ''
        if current_text != "":
            results.append(TextNode(current_text, TextType.TEXT))
        new_nodes.extend(results)
    return new_nodes
