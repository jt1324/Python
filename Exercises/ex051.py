print ('^^'*4)
print (' PA')
print ('^^'*4)

fir = int(input('Add the first term of the PA: '))
raz = int(input('Add the reason of the PA: '))
dec = fir + (10 - 1) * raz

for n in range (fir, dec, raz):
  print(n, end=' -')
print ('Done!')