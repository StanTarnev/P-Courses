import unittest

from classes.motorbike import Motorbike
from classes.engine import Engine

class TestMotorbike(unittest.TestCase):

    def setUp(self):
        self.engine = Engine()
        self.motorbike = Motorbike("Yamaha", "FZR1000", self.engine)

    def test_motorbike_can_start_engine(self):
        self.assertEqual("Vrrrmmm!", self.motorbike.start())
