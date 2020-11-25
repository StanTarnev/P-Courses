import unittest

from classes.engine import Engine

class TestEngine(unittest.TestCase):

    def setUp(self):
        self.engine = Engine()

    def test_engine_can_start(self):
        self.assertEqual("Vrrrmmm!", self.engine.start())
