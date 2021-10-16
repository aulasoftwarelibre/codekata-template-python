import unittest
from src.kata import ejemplo


class TestKata(unittest.TestCase):

    def test_ejemplo_1(self):

        self.assertEqual(True, ejemplo())

    def test_ejemplo_2(self):

        self.assertEqual(False, ejemplo())


if __name__ == '__main__':
    unittest.main()
