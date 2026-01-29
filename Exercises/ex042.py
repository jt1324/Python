print('-='*20)
print('Triangulo checker')
print('-='*20)
l1 = int(input('First line: '))
l2 = int(input('Second line: '))
l3 = int(input('Third line: '))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
  if l1 == l2 and l1 == l3:
    print ('These lines CAN MAKE a triangulo Equilatero.')
  elif l1 == l2 or l1 == l3 or l2 == l3:
    print ('These lines CAN MAKE a triangulo Isosceles.')
  else:
    print ('These lines CAN MAKE a triangulo Escaleno.')
else:
  print ('These lines CANNOT MAKE a triangulo.')
