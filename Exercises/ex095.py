data = list()
info = {}
goals = []

print ('=-'*20)
while True:
  info['name'] = str(input("Player's name: "))
  gam = int(input(f'How many games {info['name']} played? '))
  goals.clear()
  for i in range(0, gam):
    g = int(input(f'How many goals he scored on game {i+1}? '))
    goals.append(g)
  info['goals'] = goals[:]
  info['total'] = sum(goals)
  data.append(info.copy())
  while True:
    con = str(input('Do you wnat to continue? [Y/N] ')).strip().upper()[0]
    if con in 'YN':
      break
    print ('ERROR! Type only Y or N.')
  if con == 'N':
    break
  
print ('=-'*20)
print (f'{'cod':3} {'name':<10} {'goals':<10} {'total':<5}')
print('--'*18)
for i, v in enumerate(data):
  print (f'{i:>3} {v['name']:<10} {str(v['goals']):<10} {v['total']:<5}')
print('--'*18)
while True:
  while True:
    show = int(input('Show info from which player? [999 to finish]: '))
    if show in range(0, len(data)):
      break
    print (f'ERROR! Ther is no player with code {show}, Try again.')
  if show == 999:
    break
  print (f' -- showing info from player {data[show]['name']}:')
  for i, v in enumerate(data[show]['goals']):
    print (f' => In the game {i+1}, scored {v} goals.')
  print('--'*18)