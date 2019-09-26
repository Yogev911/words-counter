import unittest
from unittest.mock import patch
import json

from utilities.utils import is_url, is_path, preprocess_data


class TestUtilsMethods(unittest.TestCase):

    def test_url(self):
        st = "http://yogev.com"
        self.assertTrue(is_url(st))

        st = "thisis not url"
        self.assertFalse(is_url(st))

    def test_path(self):
        st = "/Users/yogevheskia/projects/words-counter/utilities/tests.py"
        self.assertTrue(is_path(st))

        st = "path@google.com"
        self.assertFalse(is_path(st))

    def test_preprocess_data(self):
        st = "Hi! My name is (what?), my name is (who?), my name's Slim Shady"
        data = preprocess_data(st)
        self.assertTrue("my" in data)
        self.assertTrue(data["my"] == 3)
