from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        if node.text.count(delimiter)%2 != 0:
            raise Exception(f'Invalid Markdown syntax. requires closing "{delimiter}"')
        
        working_text_list = node.text.split(delimiter)
        if working_text_list[len(working_text_list)-1] == "":
            working_text_list = working_text_list[:-1]
        working_node_list = []
        
        for index in range(len(working_text_list)):
            text = working_text_list[index]
            if index % 2 == 0:
                working_node_list.append(TextNode(text, TextType.TEXT))
            else:
                working_node_list.append(TextNode(text, text_type))
        new_nodes.extend(working_node_list)
    return new_nodes