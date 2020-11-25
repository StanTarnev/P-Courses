import unittest
import sys
sys.path.append(".")
sys.path.append("..")

from wand import *
from wizard import *
from coven import *

class TestCoven(unittest.TestCase):
    def setUp(self):
        self.broken_wand = Wand("oak", "unicorn hair")
        self.elder_wand = Wand("holly", "phoenix feather")
        self.harry = Wizard("Harry Potter", self.elder_wand)
        self.ron = Wizard("Ron Weasley", self.broken_wand)

        self.coven = Coven([self.harry, self.ron])

    def test_coven_can_cast_spell(self):
        expected = ["STUPOR", "stupor"]
        self.assertEqual(self.coven.cast_spell("stupor"), expected)
