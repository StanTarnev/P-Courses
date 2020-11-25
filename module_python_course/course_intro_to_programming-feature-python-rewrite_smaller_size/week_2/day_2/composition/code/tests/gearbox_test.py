import unittest

from classes.gearbox import Gearbox

class TestGearbox(unittest.TestCase):

    def setUp(self):
        self.gearbox = Gearbox("manual", 3)

    def test_gearbox_has_type(self):
        self.assertEqual("manual", self.gearbox.type)

    def test_gearbox_has_number_of_gears(self):
        self.assertEqual(3, self.gearbox.number_of_gears)

    def test_gearbox_starts_in_neutral(self):
        self.assertEqual("N", self.gearbox.current_gear)

    def test_gearbox_can_change_gear(self):
        self.gearbox.change_gear(2)
        self.assertEqual(2, self.gearbox.current_gear)
