print ('=='*15)
print ('      SUPER-CHEAP STORE')
print ('=='*15)

tot = 0
ovk = 0
che = 0
chen = ''
c = 0

while True:
  nam = str(input('Product name: ')).strip()
  pri = float(input('Price: R$ '))
  tot += pri
  c += 1
  if c == 1:
    che = pri
  if pri >= 1000:
    ovk += 1
  if pri < che:
    che = pri
    chen = nam
  con = str(input('Do you want to buy more? [Y/N] ')).upper().strip()[0]
  while con not in 'yYnN':
    con = str(input('Do you want to buy more? [Y/N] ')).upper().strip()[0]
  if con in 'nN':
    break
print (f'The total of your bill is R$ {tot:.2f}.')
print (f'There are {ovk} products over R$ 1.000,00.')
print (f'The cheapest product is the {chen} which cost R$ {che:.2f}.')