n1 = int(input('Add a number: '))
n2 = int(input('Add other nuber: '))
opt = 0

while opt != 5:
  print ('''
       [1] Sum
       [2] Multiply
       [3] Higher
       [4] New numbers
       [5] Leave''')
  opt = int(input('Chose one options: '))
  if opt not in (1, 2, 3, 4):
    print('Whrong number, chose one of the below.')
  if opt == 1:
    print('The sum of {} and {} is {}.'.format(n1, n2, n1+n2))
  if opt == 2:
    print('The multiplication of {} for {} is {}.'.format(n1, n2, n1*n2))
  if opt == 3:
    print('The higher value between {} and {} is {}.'.format(n1, n2, max(n1, n2)))
  if opt == 4:
    n1 = int(input('No problem, type the new first number: '))
    n2 = int(input('Type the new second number again: '))
print('You are leaving the program, bye!')