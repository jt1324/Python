from random import randint

players = dict()
game = list()

c = 1
for p in range(0, 4):
  players[(f'Player{c}')] = randint(1, 6)
  c += 1
print (players)

sorted = dict(sorted(players.items(), key=lambda item: item[1], reverse=True))

print (sorted)

ord = 1
for p in sorted:
  print(f"{ord} place: {p} with {sorted[p]}")
  ord +=1