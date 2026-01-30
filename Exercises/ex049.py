print ('++'*10)
print ('Tabuada')
print ('++'*10)

imp = int(input(' Add a number from 1 to 10: '))
for num in range(1, 11):
  print ('{} X {} = {}'.format(imp, num, (imp*num)))