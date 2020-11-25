import unittest
import sys
sys.path.append(".")
sys.path.append("..")
from team import *

class TeamTest(unittest.TestCase):

  def setUp(self):
    players = ["Beth", "Craig", "Matt", "Rick"]
    self.team = Team("CodeClan Crusaders", players, "Val Dryden")

  def test_team_has_name(self):
    self.assertEqual("CodeClan Crusaders", self.team.get_team_name())

  def test_team_has_players(self):
    self.assertEqual(4, len(self.team.get_players()))

  def test_team_has_coach(self):
    self.assertEqual("Val Dryden", self.team.get_coach())
  
  def test_check_team_has_points(self):
    self.assertEqual(0, self.team.get_points())

  def test_coach_can_be_updated(self):
    self.team.set_coach("Keith")
    self.assertEqual("Keith", self.team.get_coach())

  def test_new_player_can_be_added(self):
    new_player = "Jeff"
    self.team.add_player(new_player)
    self.assertEqual(5, len(self.team.get_players()))

  def test_check_player_in_team(self):
    self.assertEqual(True, self.team.has_player("Beth"))

  def test_if_team_wins(self):
    self.team.play_game("win")
    self.assertEqual(3, self.team.get_points())

  def test_if_team_loses(self):
    self.team.play_game("lost")
    self.assertEqual(0, self.team.get_points())

if __name__ == "__main__":
  unittest.main()