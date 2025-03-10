import unittest
from textnode import TextNode, TextType
from html_converter import text_node_to_html_node
from leafnode import LeafNode

class TestHTMLConverter(unittest.TestCase):
    def test_normal_text(self):
        node=TextNode(text="This is uncontained text", text_type=TextType.TEXT, url=None)
        expected=LeafNode(tag=None, value="This is uncontained text")
        self.assertEqual(text_node_to_html_node(node), expected)

    def test_bold_text(self):
        node = TextNode(text="This is some bold text", text_type=TextType.BOLD, url=None)
        expected = LeafNode(tag="b", value="This is some bold text")
        self.assertEqual(text_node_to_html_node(node), expected)

    def test_italic_text(self):
        node = TextNode(text="This is some italic text", text_type=TextType.ITALIC, url=None)
        expected = LeafNode(tag="i", value="This is some italic text")
        self.assertEqual(text_node_to_html_node(node), expected)

    def test_code_text(self):
        node = TextNode(text="This is a code block", text_type=TextType.CODE, url=None)
        expected = LeafNode(tag='code', value="This is a code block")
        self.assertEqual(text_node_to_html_node(node), expected)

    def test_link_text(self):
        node = TextNode(text="link to a website", text_type=TextType.LINK, url="https://www.google.com")
        expected = LeafNode(tag='a', value="link to a website", props={"href": "https://www.google.com"})
        self.assertEqual(text_node_to_html_node(node), expected)

    def test_image_text(self):
        node = TextNode(text="Picture of a doggo", text_type=TextType.IMAGE, url="https://www.google.com")
        expected = LeafNode(tag='img', value="", props={"src": "https://www.google.com", "alt": "Picture of a doggo"})
        self.assertEqual(text_node_to_html_node(node), expected)
    
    def test_text_exception(self):
        with self.assertRaises(Exception):
            node = TextNode(text="link to a website", text_type=TextType.ANCHOR, url="https://www.google.com")






if __name__ == "__main__":
    unittest.main()