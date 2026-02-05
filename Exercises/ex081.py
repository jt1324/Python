lis = []

c = 0
while True:
  n = int(input('Type a number: '))
  con = str(input('Do you want to continue? [S/N]: ')).strip().upper()[0]
  c +=1
  lis.append(n)
  if con == 'N':
    break
print ('=='*15)
print (f'You typed {c} numbers.')
print (f'The nubmers in order are: {sorted(lis)}.')
if 5 in lis:
  print ('You have typed the number 5.')
else:
  print ('The number 5 is not in the list.')