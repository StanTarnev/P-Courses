from person import *

class Agent(Person):

  def __init__(self, first_name, last_name):
    Person.__init__(self, first_name, last_name)

  def talk(self):
    return f"The name's {self.last_name}, {self.first_name} {self.last_name}"
