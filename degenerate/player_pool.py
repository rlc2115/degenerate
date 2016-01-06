import csv

from degenerate import Player

class PlayerPool:
  def from_csv(self, filename):
    self.players = []

    with open(filename, 'rb') as csv_file:
      csv_data = csv.DictReader(csv_file, skipinitialspace=True)

      for row in csv_data:
        self.players.append(Player(row))

    return self

  def all_players(self):
    return self.players

  def banned_players(self):
    return filter(lambda x: x.ban, self.players)

  def locked_players(self):
    return filter(lambda x: x.lock, self.players)

  def as_json(self):
    return map(lambda x: x.__json___(), self.players)
