import unittest
from link_extractor import extract_markdown_links

class TestLinkExtractor(unittest.TestCase):
    def test_link_extractor(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        self.assertEqual(extract_markdown_links(text), [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")])
    

if __name__ == "__main__":
    unittest.main()