import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(props = {"href": "https://www.google.com","target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')

    #def test_to_html(self):
    #    node = HTMLNode(props = {"href": "https://www.google.com","target": "_blank"})
    #    with self.assertRaises(NotImplementedError):
    #        node.to_html()

    def test_children(self):
        node = HTMLNode(children = "")
        self.assertEqual(node.children, [])
    
    def test_props(self):
        node = HTMLNode(props = "")
        self.assertEqual(node.props, {})

if __name__ == "__main__":
    unittest.main()