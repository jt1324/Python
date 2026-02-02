print ('_-'*10)
print ('Fibonacci')
print ('_-'*10)

n1 = int(input('Add ho wmany results you want to see: '))
t1 = 0
t2 = 1

print ('{} - {}'.format(t1, t2), end='')
c = 3

while c <= n1:
  t3 = t1 + t2
  print (' - {}'.format(t3), end='')
  t1 = t2
  t2 = t3
  c += 1
print (' - End.')

