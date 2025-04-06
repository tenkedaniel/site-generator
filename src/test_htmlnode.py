import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    
    def test_props_to_html_empty(self):
        # Test with no props
        node = HTMLNode("p", "Hello, world!", None, {})
        self.assertEqual(node.props_to_html(), "")
        
    def test_props_to_html_single_prop(self):
        # Test with a single prop
        node = HTMLNode("a", "Click me", None, {"href": "https://example.com"})
        self.assertEqual(node.props_to_html(), ' href="https://example.com"')
        
    def test_props_to_html_multiple_props(self):
        # Test with multiple props
        node = HTMLNode(
            "a", 
            "Google", 
            None, 
            {"href": "https://www.google.com", "target": "_blank"}
        )
        # Note: Since dictionaries are unordered, you might need to check for both possible orders
        result = node.props_to_html()
        self.assertTrue(
            result == ' href="https://www.google.com" target="_blank"' or 
            result == ' target="_blank" href="https://www.google.com"'
        )

if __name__ == "__main__":
    unittest.main()