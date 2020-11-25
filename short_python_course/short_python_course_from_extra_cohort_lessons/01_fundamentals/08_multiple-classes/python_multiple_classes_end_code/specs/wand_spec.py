import unittest
import sys
sys.path.append(".")
sys.path.append("..")

from wand import *

class TestWand(unittest.TestCase):
    def setUp(self):
        self.wand = Wand("holly", "phoenix feather")

    def test_wand_wood(self):
        self.assertEqual(self.wand.wood, "holly")

    def test_wand_core(self):
        self.assertEqual(self.wand.core, "phoenix feather")

if __name__ == '__main__':
    unittest.main()
