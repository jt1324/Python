#from math import factorial

num = int(input('Type a number: '))
fac = num
cal = 1

while fac > 0:
  print('Preparing the factorial {}'.format(fac), end='')
  print(' x ' if fac > 1 else ' = ', end='')
  cal *= fac
  fac -= 1
print('The factorial of {} is {}'. format(num, cal))