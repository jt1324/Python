print ('=-'*10)
print ('  PA  ')
print('-='*10)

v1 = int(input('Add the first number: '))
v2 = int(input('Add the factor: '))
t = v1
c = 1
qt = 0
more = 10

while more != 0:
  qt = qt + more
  while c < qt:
    t += v2
    c += 1
    print (t, end=' - ')
  print ('Pause')
  more = int(input('How many results do yu want to see more? '))
print ('End!')