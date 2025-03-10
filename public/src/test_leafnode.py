import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        node = LeafNode(tag = "a", value="This is an anchor tag", props={"href":"https://www.google.com"})
        self.assertEqual(node.to_html(), f'<a href="https://www.google.com">This is an anchor tag</a>')
    
    def test_no_value(self):
        with self.assertRaises(ValueError):
            node = LeafNode(tag = "a", value=None, props={"href":"https://www.google.com"})

    def test_plain_text(self):
        node = LeafNode(tag = None, value="this is some plain text", props=None)
        self.assertEqual(node.to_html(), "this is some plain text")

    if __name__ == "__main__":
        unittest.main()