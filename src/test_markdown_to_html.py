import unittest
from markdown_to_html import markdown_to_html_node
from parentnode import ParentNode

class TestMarkdown_to_HTML_Node(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph\ntext in a p\ntag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_heading(self):
        md = """
        # Heading Level 1

## Heading Level 2

### Heading Level 3
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>Heading Level 1</h1><h2>Heading Level 2</h2><h3>Heading Level 3</h3></div>",
        )

    def test_blockquote(self):
        md = """
> This is a quote block
> with multiple lines
> of quoted text
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a quote block\nwith multiple lines\nof quoted text</blockquote></div>",
        )

    def test_ul(self):
        md = """
- Unordered list item 1
- Unordered list item 2
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>Unordered list item 1</li><li>Unordered list item 2</li></ul></div>",
        )

    def test_ol(self):
        md = """
1. Unordered list item 1
2. Unordered list item 2
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li> Unordered list item 1</li><li> Unordered list item 2</li></ol></div>",
        )