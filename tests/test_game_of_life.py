import unittest
from src.game_of_life import GameOfLife


class TestGameOfLife(unittest.TestCase):
    def test_next_generation(self):
        universe = GameOfLife().next_generation()

        self.assertEqual("foo", universe)


if __name__ == '__main__':
    unittest.main()
