import random

com = random.randint(1, 10)
gue = int(input('Try to guess a number form 1 to 10: '))
tr = 0

while gue != com:
  gue = int(input('Sorry, wrong number, try again: '))
  tr += 1
print('Congrats, the number is {}! You guessed in {} tries.'.format(com, tr))