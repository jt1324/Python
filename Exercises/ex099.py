from random import randint
from time import sleep

def values(*num):
  print ('-='*25)
  print ('Checking the available numbers...')
  for nu in num:
    print (f'{nu} ', end='', flush=True)
    sleep(0.25)
  print (f'Were provided {len(num)} values in total.')
  print (f'The highest number is {max(num)}.')
  # print ('-='*25)

values (randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9))
values (4, 7, 0)
values (1, 2)
values (6)
values (0)