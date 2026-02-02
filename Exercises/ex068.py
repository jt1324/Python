import random

print ('=-'*12)
print ("LET'S PLAY EVEN OR ODD")
print ('=-'*12)
res = ''
com = random.randint(1, 10)
tot = 0
win = 0

while True:
  pla = int(input('Type a number: '))
  eo = str(input('Even or Odd [E/O]:')).upper().strip()[0]
  tot = pla+com
  if tot % 2 == 0:
    res = 'EVEN'
    print ('--'*12)
    print (f'You played {pla} and the computer played {com}. Total is {pla+com} is {res}')
    print ('--'*12)
    if eo in 'Ee':
      print ('You WIN!')
      print ("Let's play again...")
      win += 1
    else:
      print ('You LOSE!')
      break
  else:
    res = 'ODD'
    print ('--'*12)
    print (f'You played {pla} and the computer played {com}. Total is {pla+com} is {res}')
    print ('--'*12)
    if eo in 'Oo':
      print ('You WIN!')
      print ("Let's play again...")
      win += 1
    else:
      print ('You LOSE!')
      break
print (f'Thank you for playing, you won {win} times!')