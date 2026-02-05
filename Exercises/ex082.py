l1 = []
le = []
lo = []

while True:
  n = int(input('Type a number: '))
  l1.append(n)
  c = str(input('Do you want to continue? [S/N]: ')).strip().upper()[0]
  if c == 'N':
    break
print ('--'*15)
print (f'The complete list is {l1}')

for l in l1:
  if l % 2 == 0:
    le.append(l)
  else:
    lo.append(l)

print (f'The EVEN list is {le}.')
print (f'The ODD list is {lo}.')