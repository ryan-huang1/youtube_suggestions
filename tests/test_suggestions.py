import unittest
from youtube_suggestions import get_suggestions

class TestYouTubeSuggestions(unittest.TestCase):
    def test_get_suggestions(self):
        suggestions = get_suggestions("python programming")
        self.assertIsInstance(suggestions, list)
        self.assertTrue(len(suggestions) > 0)

    def test_empty_query(self):
        with self.assertRaises(ValueError):
            get_suggestions("")
