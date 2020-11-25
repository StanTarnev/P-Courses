import unittest
import sys


from app.models.rps import *
from app.models.player import *

class RpsTest(unittest.TestCase):

    def setUp(self):
        self.game = Rps()
        self.player1 = Player(1, "Rock")
        self.player2 = Player(2, "Scissors")

    def test_player1_win(self):
        winner = self.game.check_win(self.player1, self.player2)
        self.assertEquals(1, winner.number)

    def test_player2_win(self):
        self.player2.hand = "Paper"
        winner = self.game.check_win(self.player1, self.player2)
        self.assertEquals(2, winner.number)

    def test_draw(self):
        self.player2.hand = "Rock"
        winner = self.game.check_win(self.player1, self.player2)
        self.assertEquals("Draw", winner.hand)

    def test_incorrectInput(self):
        self.player2.hand = "Banana"
        winner = self.game.check_win(self.player1, self.player2)
        self.assertEquals(None, winner)
