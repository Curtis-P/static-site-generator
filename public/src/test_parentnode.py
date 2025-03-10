import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_empty_children(self):
        node = ParentNode("div", [], None)
        self.assertEqual(node.to_html(), f"<div></div>")
    def test_no_children(self):
        with self.assertRaises(ValueError):
            node = ParentNode("div", None, None)
    def test_no_tag(self):
        with self.assertRaises(ValueError):
            node = ParentNode(None, [], None)            
    def test_props_none(self):
        node = ParentNode("div", [LeafNode("span", "hello")], None)
        self.assertEqual(node.to_html(),f"<div><span>hello</span></div>")
    def test_large_node(self):
        node = ParentNode("p",[LeafNode("b", "Bold text"),LeafNode(None, "Normal text"),LeafNode("i", "italic text"),LeafNode(None, "Normal text"),],)
        self.assertEqual(node.to_html(), f"<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")
    def test_nested_nodes(self):
        inner_node = ParentNode("p", [LeafNode("b", "Bold Text")], None)
        outer_node = ParentNode("div", [inner_node], None)
        self.assertEqual(outer_node.to_html(), "<div><p><b>Bold Text</b></p></div>")


if __name__ == "__main__":
    unittest.main()