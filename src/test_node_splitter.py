import unittest
from textnode import TextNode, TextType
from node_splitter import split_nodes_delimiter

class TestNodeSplitter(unittest.TestCase):
    def test_text_delimiter(self):
        old_nodes = [TextNode("Just a plain text node", TextType.TEXT)]
        delimiter = "`"
        text_type = TextType.TEXT
        self.assertEqual(split_nodes_delimiter(old_nodes, delimiter, text_type), [TextNode("Just a plain text node", TextType.TEXT)])

    def test_code_delimiter(self):
        old_nodes = [TextNode("Just a `plain` text node", TextType.TEXT)]
        delimiter = "`"
        text_type = TextType.CODE
        self.assertEqual(split_nodes_delimiter(old_nodes, delimiter, text_type), [TextNode("Just a ", TextType.TEXT), TextNode("plain", TextType.CODE), TextNode(" text node", TextType.TEXT)])
    
    def test_bold_delimiter(self):
        old_nodes = [TextNode("Just a **plain** text node", TextType.TEXT)]
        delimiter = "**"
        text_type = TextType.BOLD
        self.assertEqual(split_nodes_delimiter(old_nodes, delimiter, text_type), [TextNode("Just a ", TextType.TEXT), TextNode("plain", TextType.BOLD), TextNode(" text node", TextType.TEXT)])
    
    def test_italic_delimiter(self):
        old_nodes = [TextNode("Just a *plain* text node", TextType.TEXT)]
        delimiter = "*"
        text_type = TextType.ITALIC
        self.assertEqual(split_nodes_delimiter(old_nodes, delimiter, text_type), [TextNode("Just a ", TextType.TEXT), TextNode("plain", TextType.ITALIC), TextNode(" text node", TextType.TEXT)])
    
    def test_underscore_italic_delimiter(self):
        old_nodes = [TextNode("Just a _plain _ text node", TextType.TEXT)]
        delimiter = "_"
        text_type = TextType.ITALIC
        self.assertEqual(split_nodes_delimiter(old_nodes, delimiter, text_type), [TextNode("Just a ", TextType.TEXT), TextNode("plain ", TextType.ITALIC), TextNode(" text node", TextType.TEXT)])
    
    def test_invalid_delimiter_count(self):
        old_nodes = [TextNode("Just a *plain text node", TextType.TEXT)]
        delimiter = "*"
        text_type = TextType.ITALIC
        with self.assertRaises(Exception):
            split_nodes_delimiter(old_nodes,delimiter,text_type)
    
    def test_already_formatted_node(self):
        old_nodes = [TextNode("Already bold", TextType.BOLD)]
        delimiter = "**"
        text_type = TextType.BOLD
        self.assertEqual(split_nodes_delimiter(old_nodes, delimiter, text_type), [TextNode("Already bold", TextType.BOLD)])

    def test_multiple_delimiters(self):
        old_nodes = [TextNode("Hello `world` and `python`", TextType.TEXT)]
        delimiter = "`"
        text_type = TextType.CODE
        self.assertEqual(split_nodes_delimiter(old_nodes, delimiter, text_type), [TextNode("Hello ",TextType.TEXT), TextNode("world",TextType.CODE), TextNode(" and ",TextType.TEXT), TextNode("python",TextType.CODE)])


if __name__ == "__main__":
    unittest.main()
