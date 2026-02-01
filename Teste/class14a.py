# WHILE

# using FOR
for c in range(1, 5):
  print(c)  
print('End!')

# using WHILE
c = 1
while c < 5:
  print (c)
  c+= 1
print('End!!!')


n = 1
while n != 0:
  n = int(input('Type a number: '))
print ('End!')

r = 'S'
while r == 'S':
  n = int(input('Type a number: '))
  r = str(input('Do you want to continue? [S/N]: ')).upper()
print('OK, end!')

num = 1
odd = even = 0
while n != 0:
  n = int(input('Type a number: '))
  if n != 0:
    if  n % 2 == 0:
      even += 1
    else:
      odd += 1
print ('You typed {} even numbers and {} odd numbers.'.format(even, odd))