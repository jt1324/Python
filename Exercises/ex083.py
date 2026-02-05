import math

l = 0
r = 0

ex = str(input('Type a math expression: '))

for e in ex:
  if e == '(':
    l += 1
  elif e == ')':
    r += 1

if l == r:
  print('Your math expression is correct.')
else:
  print('Your mats expression is incorrect.')

