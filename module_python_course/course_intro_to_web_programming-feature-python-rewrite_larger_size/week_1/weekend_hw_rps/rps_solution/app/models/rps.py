import random
from app.models.player import *

class Rps:

    def __init__(self):
        self.win_lookup = {
        "scissors": "paper",
        "paper": "rock",
        "rock": "scissors"
        }

    def check_win(self, player1, player2):
        hand1 = player1.hand.lower()
        hand2 = player2.hand.lower()

        winner = None

        if self.win_lookup.get(hand1) == hand2:
            winner = player1
        elif self.win_lookup.get(hand2) == hand1:
            winner = player2

        return winner

    def generate_computer_player(self):
        all_moves = list(self.win_lookup.keys())
        computer_hand = random.choice(all_moves)
        computer = Player("Computer", computer_hand)
        return computer
