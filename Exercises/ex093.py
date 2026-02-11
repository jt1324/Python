info = {}
goals = []

info['name'] = str(input("Player's name: "))
gam = int(input(f'How many games {info['name']} played? '))

for i in range(0, gam):
  g = int(input(f'How many goals he scored on game {i+1}? '))
  goals.append(g)
  
info['goals'] = goals[:]
info['total'] = sum(goals)
print ('=-'*20)
print (info)
print ('=-'*20)

for k, v in info.items():
  print (f' -The info {k} has the value {v}.')
print ('=-'*20)
print (f'The player {info['name']} played {gam} games.')

for i, v in enumerate(info['goals']):
  print (f' => In the game {i+1}, scored {v} goals.')
print (f'Was a total of {info['total']} goals.')