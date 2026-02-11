info = {}
goals = []

info['name'] = str(input("Player's name: "))
gam = int(input(f'How many games {info['name']} played? '))
c = 1
t = 0
for i in range(0, gam):
  g = int(input(f'How many goals he scored on game {c}? '))
  goals.append(g)
  c += 1
  if t == 0:
    t = g
  else:
    t += g
info['goals'] = goals
info['total'] = t
print ('=-'*20)
print (info)
print ('=-'*20)

for k, v in info.items():
  print (f' -The info {k} has the value {v}.')
print ('=-'*20)
print (f'The player {info['name']} played {gam} games.')
s = 0
p = 1
for v in info['goals']:
  print (f' => In the game {p}, scored {info['goals'][s]} goals.')
  p += 1
  s += 1
print (f'Was a total of {info['total']} goals.')