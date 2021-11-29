import unittest

from src.kata import is_true


class TestKata(unittest.TestCase):
    def test_is_true(self):
        self.assertEqual(True, is_true())

    def test_is_true_again(self):
        self.assertNotEqual(False, is_true())
