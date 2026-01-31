print ('People analysis')
print ('+='*10)

tage = 0
hage = 0
nold = ''
f20 = 0
for p in range (1, 5):
  print('-- Person {} --'.format(p))
  n1 = str(input('Name: ').strip())
  a1 = int(input('Age: '))
  g1 = str(input('Gender (M or F): '.strip()))
  tage += a1
  if p == 1 and g1 in 'Mm':
    hage = a1
    nold = n1
  if g1 in 'Mm' and a1 > hage:
    hage = a1
    nold = n1
  if g1 in 'Ff' and a1 < 20:
    f20 += 1
print ('The average of age from the group is {}.'.format(tage/4))
print ('The oldest man is {} years old and his name is {}.'.format(hage, nold))
print ('The group has {} females under 20 year old.'.format(f20))