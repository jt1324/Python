from random import randint
from time import sleep

# numbers = list()
# # su = 0

# def sort (*num):
#   su = 0
#   print ('Getting 5 numbers from the list: ', end='')
#   for n in num:
#     numbers.append(n)
#     print (f'{n} ', end='', flush=True)
#     sleep(0.25)
#     if n % 2 == 0:
#       su += n

#   print ('DONE!')
#   print (f'The sum of EVEN numbers of {numbers} is {su}.')


# sort (randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9))

# teacher's solution

def sort(list):
  print ('Getting 5 numbers from the list: ', end='')
  for nu in range(0, 5):
    n = randint(1, 10)
    list.append(n)
    print (f'{n} ', end='', flush = True)
    sleep(0.3)
  print('Ready!')


def even(num):
  ev = 0
  for n in num:
    if n % 2 == 0:
      ev += n
  print (f'The sum of EVEN numbers of {numbers} is {ev}.')

numbers = list()
sort(numbers)
even(numbers)


