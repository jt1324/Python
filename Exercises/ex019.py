import random
sor = int(random.randint(1, 4))
n1 = 'Joao'
n2 = 'Jose'
n3 = 'Pedro'
n4 = 'Dunha'
if sor == 1:
  print('Who will clean the boar is {}.'. format(n1))
elif sor == 2:
  print('Who will clean the boar is {}.'. format(n2))
elif sor == 3:
  print('Who will clean the boar is {}.'. format(n3))
else:
  print('Who will clean the boar is {}.'. format(n4))

# Othere way to do
list = [n1, n2, n3, n4]
cho = random.choice(list)
print('The chosed is {}'.format(cho))
