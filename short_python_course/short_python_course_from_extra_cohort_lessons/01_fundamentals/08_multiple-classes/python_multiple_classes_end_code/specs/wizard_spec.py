import unittest
import sys
sys.path.append(".")
sys.path.append("..")

from wand import *
from wizard import *

class TestWizard(unittest.TestCase):
    def setUp(self):
        self.broken_wand = Wand("oak", "unicorn hair")
        self.elder_wand = Wand("holly", "phoenix feather")
        self.ron = Wizard("Ron Weasley", self.broken_wand)
        self.harry = Wizard("Harry Potter", self.elder_wand)

    def test_wizard_name(self):
        self.assertEqual(self.ron.name, "Ron Weasley")

    def test_can_cast_spell(self):
        self.assertEqual(self.ron.cast_spell("stupor"), "stupor")

    def test_can_cast_stronger_spell(self):
        self.assertEqual(self.harry.cast_spell("expecto patronum"), "EXPECTO PATRONUM")

if __name__ == '__main__':
    unittest.main()
