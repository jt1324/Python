from random import randint
from time import sleep

players = dict()
game = list()

c = 1
for p in range(0, 4):
  players[(f'Player{c}')] = randint(1, 6)
  c += 1

o = 1
for p in players:
  print(f"{p} got {players[p]}")
  o +=1
  sleep(1)
  
sort = dict(sorted(players.items(), key=lambda item: item[1], reverse=True))

print (' xxxx Players Ranking! xxxx ')
ord = 1
for p in sort:
  print(f"{ord} place: {p} with {sort[p]}")
  ord +=1
  sleep(1)


# ----------------------------------------------------------
# VIDEO SOLUTION

from operator import itemgetter

jogo = {'player1': randint(1, 6),
        'player2': randint(1, 6),
        'player3': randint(1, 6),
        'player4': randint(1, 6)}
rank = list()
print('Numbers generated:')
for k, v in jogo.items():
  print (f'{k} got {v}')
  sleep(1)
rank = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('=+'*20)
print('       == RANKING ==  ')
for i, v in enumerate(rank):
  print (f' {i+1}o place: {v[0]} with {v[1]}.')
  sleep(1)
  