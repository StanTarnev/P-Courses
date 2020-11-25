class Student:

  def __init__(self, name, cohort):
    self.name = name
    self.cohort = int(cohort)

  def set_name(self, name):
    self.name = name

  def get_name(self):
    return self.name

  def set_cohort(self, cohort):
    self.cohort = cohort

  def get_cohort(self):
    return self.cohort

  def talk(self):
    return "I can talk"

  def say_favourite_language(self, language):
    return "I love " + language
