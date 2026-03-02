from rich.panel import Panel
from rich import print

class Gamer:
  def __init__(self, name, nick):
    self.name = name
    self.nick = nick
    self.games = []

  
  def add_fav(self, game):
    self.games.append(game)
  
  def data(self):
    games_list = '\n'.join([f":video_game: [blue]{game}[/]" for game in sorted(self.games)])
    print(Panel(f"Real name: [bold blue on white]{self.name}[/]\nFavorite games:\n{games_list}", title=f"Player <{self.nick}>"))
  
p1 = Gamer('Jean Toneli', 'JC_destroyer')
p1.add_fav('Puzzle & Survival')
p1.add_fav('GTA')
p1.add_fav('Guitar Hero')
p1.add_fav('Enduro')
p1.data()

p2 = Gamer('Tis', 'Doidona')
p2.add_fav('Pac-man')
p2.add_fav('Rock Band')
p2.data()