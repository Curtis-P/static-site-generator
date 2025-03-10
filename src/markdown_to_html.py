from markdown_blocks import BlockType, markdown_to_blocks, block_to_block_type
from htmlnode import HTMLNode
from text_converter import text_to_textnodes
from html_converter import text_node_to_html_node
from parentnode import ParentNode
from leafnode import LeafNode
from textnode import TextNode, TextType

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    container = ParentNode("div", [])
    for block in blocks:
        block_type = block_to_block_type(block)
        container.children.append(block_to_parent_node(block, block_type))
    return container

def text_to_children(text):
    retList = []
    textNodes = text_to_textnodes(text)
    for node in textNodes:
        retList.append(text_node_to_html_node(node))
    return retList

def block_to_parent_node(block, block_type):
    match(block_type):
        case(BlockType.PARAGRAPH):
            return ParentNode("p", text_to_children(block))
        case(BlockType.HEADING):
            return create_heading_node(block)
        case(BlockType.CODE):           
            node = TextNode(block[4:-3], TextType.CODE)
            node = text_node_to_html_node(node)
            return ParentNode("pre", [node])
        case(BlockType.QUOTE):
            nodes = text_to_children(clean_quote_block(block))
            return ParentNode("blockquote", nodes)
        case(BlockType.OLIST):
            return ParentNode("ol", create_list_item_node(block))
        case(BlockType.ULIST):
            return ParentNode("ul", create_list_item_node(block))


def create_heading_node(block):
    level = 0
    for char in block:
        if char =="#":
            level += 1
        else: 
            break
    if level < 1:
        level  = 1
    if level > 6:
        level = 6
    content = block[level:].strip()
    children = text_to_children(content)
    heading_tag = f"h{level}"
    return HTMLNode(heading_tag, None, children, None)

def create_list_item_node(block):
    list_children = []
    lines = block.split("\n")
    for line in lines:
        list_children.append(LeafNode("li", line[2:]))
    return list_children

def clean_quote_block(block):
    cleaned_lines = []
    lines = block.split("\n")
    for line in lines:
        if line.startswith(">"):
            line = line[1:]
            if line and line[0] == " ":
                line = line[1:]
        cleaned_lines.append(line)
    return "\n".join(cleaned_lines)
