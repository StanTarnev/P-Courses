import unittest
import sys
sys.path.append('.')
sys.path.append('..')
from agent import *

class TestAgent(unittest.TestCase):

  def setUp(self):
    self.agent = Agent("Brooke", "Bond")

  def test_agent_has_first_name(self):
    self.assertEqual("Brooke", self.agent.get_first_name())

  def test_agent_has_last_name(self):
    self.assertEqual("Bond", self.agent.get_last_name())

  def test_agent_can_talk(self):
    self.assertEqual("The name's Bond, Brooke Bond", self.agent.talk())

if __name__ == '__main__':
  unittest.main()