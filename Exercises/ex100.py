from random import randint
from time import sleep

numbers = list()
# su = 0

def sort (*num):
  su = 0
  print ('Getting 5 numbers from the list: ', end='')
  for n in num:
    numbers.append(n)
    print (f'{n} ', end='', flush=True)
    sleep(0.25)
    if n % 2 == 0:
      su += n

  print ('DONE!')
  print (f'The sum of EVEN numbers of {numbers} is {su}.')


sort (randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9))




