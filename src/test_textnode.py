import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
        
    def test_noteq(self):
        node = TextNode("This is a text node", TextType.NORMAL)
        node2 = TextNode("This is another text node", TextType.BOLD)
        self.assertNotEqual(node, node2)
        
    def test_eq_text(self):
        node = TextNode("This is a text node", TextType.NORMAL)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node.text, node2.text)
        
    def test_eq_url(self):
        node = TextNode("search site", TextType.LINK, "http://google.com")
        node2 = TextNode("search site", TextType.LINK, "http://google.com")
        self.assertEqual(node.url, node2.url)

if __name__ == "__main__":
    unittest.main()