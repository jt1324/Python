print ('¬¬'*6)
print ('   Cousin')
print ('¬¬'*6)

cou = 0
num = int(input(('Add a number: ')))
for c in range (1, num+1):
  if num % c == 0:
    cou += 1
    print ('\033[0;33m{}\033[m'.format(c), end=" ")
  else:
    print ('\033[0;31m{}\033[m'.format(c), end=" ")

if cou >2:
  print ('\nThe number {} was divisible {} times.'.format(num, cou))
  print ("So it is NOT a cousin number!")
else:
  print("\nThe number {} was only divisible by 1 and itself, so it IS a cousin number!".format(num))