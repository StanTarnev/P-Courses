class Team:

  def __init__(self, team_name, players, coach_name):
    self.team_name = team_name
    self.players = players
    self.coach = coach_name
    self.points = 0

  def get_team_name(self):
    return self.team_name

  def get_players(self):
    return self.players

  def get_coach(self):
    return self.coach

  def get_points(self):
    return self.points

  def set_team_name(self, team_name):
    self.team_name = team_name

  def set_coach(self, coach):
    self.coach = coach

  def add_player(self, new_player):
    self.players.append(new_player)

  def has_player(self, player):
    return player in self.players

  def play_game(self, result):
    if (result.lower() == "win"):
      self.points += 3
