from textnode import TextNode, TextType
from link_extractor import extract_markdown_links

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        links = extract_markdown_links(node.text) #(list of tupples (hyperlink, url))
        if not links:
            new_nodes.append(node)
            continue

        results = []
        current_text = node.text
        for hyper, url in links:
            full = f"[{hyper}]({url})"
            parts = current_text.split(full, 1)
            if parts[0]:
                results.append(TextNode(parts[0], TextType.TEXT))
            results.append(TextNode(hyper, TextType.LINK, url))
            if len(parts) > 1:
                current_text = parts[1]
            else: 
                current_text = ''
        if current_text != "":
            results.append(TextNode(current_text, TextType.TEXT))
        new_nodes.extend(results)
    return new_nodes