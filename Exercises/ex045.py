import random

print('--'*20)
print('Rock, Paper, Cisor GAME')
print('--'*20)

cho = int(input('Rock = 1, Paper = 2, Cisor = 3: '))
pc = random.randint(1, 3)

if cho == 1 and pc == 2:
  print ('You choose Rock and the Computer choose Paper, YOU LOST!')
elif cho == 2 and pc == 1:
  print ('You choose Paper and the Computer choose Rock, YOU WIN!')
elif cho == 1 and pc == 3:
  print ('You choose Rock and the Computer choose Cisor, YOU WIN!')
elif cho == 3 and pc == 1:
  print ('You choose Cisor and the Computer choose Rock, YOU LOST!')
elif cho == 2 and pc == 3:
  print ('You choose Paper and the Computer choose Cisor, YOU LOST!')
elif cho == 3 and pc == 2:
  print ('You choose Cisor and the Computer choose Paper, YOU MIN!')
else:
  print ('DRAW!')