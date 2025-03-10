import unittest
from image_extractor import extract_markdown_images


class TestImageExtractor(unittest.TestCase):
    def test_img(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        self.assertEqual(extract_markdown_images(text), [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")])

    def test_no_img(self):
        text = "This is text with a ![invalid img]"
        self.assertEqual(extract_markdown_images(text), [])
    def test_no_alt(self):
        text = "This is text with a !(https://i.imgur.com/aKaOqIh.gif)"
        self.assertEqual(extract_markdown_images(text), [])
    def test_empty_string(self):
        text = ""
        self.assertEqual(extract_markdown_images(text), [])
if __name__ == "__main__":
    unittest.main()
