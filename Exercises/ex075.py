n1 = int(input('Type a number: '))
n2 = int(input('Type other number: '))
n3 = int(input('Type another number: '))
n4 = int(input('Last one: '))

num = (n1, n2, n3, n4)

print (f'You typed the numbers: {num}.')

if 9 in num:
  print (f'The number 9 was typed {num.count(9)} times.')
else:
  print ("The number 9 wasn't typed.")

if 3 in num:
  print (f'Ther number 3 is on position {num.index(3)+1}.')
else:
  print ("The number 3 wasn't typed.")

print ('The even numbers are: ', end='')
for n in num:
  if n % 2 == 0:
    print (f'{n} ', end='')