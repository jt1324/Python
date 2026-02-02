print ('=-'*10)
print ('  PA  ')
print('-='*10)

v1 = int(input('Add the first number: '))
v2 = int(input('Add the factor: '))

c = 1
f = v1
while c < 10:
  v1 = (v1+v2)
  c += 1
  print (v1, end=' - ')
print ('End.')