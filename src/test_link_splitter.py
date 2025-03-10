import unittest
from textnode import TextNode, TextType
from node_splitter_links import split_nodes_link

class TestLinkSplitter(unittest.TestCase):
    def test_empty_text(self):
        node = TextNode('', TextType.TEXT)
        split_node = split_nodes_link([node])
        self.assertEqual(split_node, [node])

    def test_no_link(self): #
        node = TextNode("Just plain text here", TextType.TEXT)
        split_node = split_nodes_link([node])
        self.assertEqual(split_node, [node])
        
    def test_link_start(self): #
        node = TextNode("[link_text](url) followed by text", TextType.TEXT)
        split_node = split_nodes_link([node])
        self.assertEqual(split_node, [TextNode("link_text", TextType.LINK, "url"),TextNode(" followed by text", TextType.TEXT)])

    def test_link_end(self):
        node = TextNode("Text followed by [link_text](url)", TextType.TEXT)
        split_node = split_nodes_link([node])
        self.assertEqual(split_node, [TextNode("Text followed by ", TextType.TEXT), TextNode("link_text", TextType.LINK, "url"),])

    def test_link_multiple(self): 
        node = TextNode("[link_text1](url1)[link_text2](url2)", TextType.TEXT)
        split_node = split_nodes_link([node])
        self.assertEqual(split_node, [TextNode('link_text1', TextType.LINK, 'url1'), TextNode('link_text2', TextType.LINK, 'url2')])

    def test_link_empty_children(self): 
        node= TextNode("[](url)", TextType.TEXT)
        split_node = split_nodes_link([node])
        self.assertEqual(split_node, [TextNode('', TextType.LINK, 'url')])

    def test_link_non_text_node(self): 
        node = TextNode('this is a block of code', TextType.CODE)
        split_node= split_nodes_link([node])
        self.assertEqual(split_node, [node])
        

if __name__ == "__main__":
    unittest.main()