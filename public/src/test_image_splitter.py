import unittest
from textnode import TextNode, TextType
from image_extractor import extract_markdown_images
from node_splitter_images import split_nodes_image

class TestImageSplitter(unittest.TestCase):
    def test_empty_text(self):
        node = TextNode('', TextType.TEXT)
        split_node = split_nodes_image([node])
        self.assertEqual(split_node, [node])

    def test_no_image(self): #
        node = TextNode("Just plain text here", TextType.TEXT)
        split_node = split_nodes_image([node])
        self.assertEqual(split_node, [node])
        
    def test_image_start(self): #
        node = TextNode("![image](url) followed by text", TextType.TEXT)
        split_node = split_nodes_image([node])
        self.assertEqual(split_node, [TextNode("image", TextType.IMAGE, "url"),TextNode(" followed by text", TextType.TEXT)])

    def test_image_end(self):
        node = TextNode("Text followed by ![image](url)", TextType.TEXT)
        split_node = split_nodes_image([node])
        self.assertEqual(split_node, [TextNode("Text followed by ", TextType.TEXT), TextNode("image", TextType.IMAGE, "url"),])

    def test_image_multiple(self): 
        node = TextNode("![img1](url1)![img2](url2)", TextType.TEXT)
        split_node = split_nodes_image([node])
        self.assertEqual(split_node, [TextNode('img1', TextType.IMAGE, 'url1'), TextNode('img2', TextType.IMAGE, 'url2')])

    def test_image_empty_children(self): 
        node= TextNode("![](url)", TextType.TEXT)
        split_node = split_nodes_image([node])
        self.assertEqual(split_node, [TextNode('', TextType.IMAGE, 'url')])

    def test_image_non_text_node(self): 
        node = TextNode('this is a block of code', TextType.CODE)
        split_node= split_nodes_image([node])
        self.assertEqual(split_node, [node])



if __name__ == "__main__":
    unittest.main()