print ('=='*10)
print ('Sum numbers')
print ('=='*10)

s = 0
for nu in range(1, 7):
  n = int(input('Add a number: '))
  if n % 2 == 0:
    s += n
print ('The sum is {}.'.format(s))