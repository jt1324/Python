n1 = int(input('Add a number: '))
n2 = int(input('Add other nuber: '))
opt = int(input('Chose an options [1]Sum, [2]Multiply, [3]Higher, [4]New numbers, [5]Leave: '))

while opt != 5:
  if opt not in (1, 2, 3, 4):
    opt = int(input('Whrong number, chose one of [1]Sum, [2]Multiply, [3]Higher, [4]New numbers, [5]Leave: '))
  if opt == 1:
    print('The sum of {} and {} is {}.'.format(n1, n2, n1+n2))
    opt = int(input('Chose an options [1]Sum, [2]Multiply, [3]Higher, [4]New numbers, [5]Leave: ')) 
  if opt == 2:
    print('The multiplication of {} for {} is {}.'.format(n1, n2, n1*n2))
    opt = int(input('Chose an options [1]Sum, [2]Multiply, [3]Higher, [4]New numbers, [5]Leave: '))
  if opt == 3:
    print('The higher value between {} and {} is {}.'.format(n1, n2, max(n1, n2)))
    opt = int(input('Chose an options [1]Sum, [2]Multiply, [3]Higher, [4]New numbers, [5]Leave: '))
  if opt == 4:
    n1 = int(input('No problem, type the new first number: '))
    n2 = int(input('Type the new second number again: '))
    opt = int(input('Chose an option: [1]Sum, [2]Multiply, [3]Higher, [4]New numbers, [5]Leave'))
print('You are leaving the program, bye!')