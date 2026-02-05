lib = list()

while True:
  n = int(input('Type a number: '))
  if n in lib:
    print('Dupe number. Not added.')
  else:
    lib.append(n)
    print ('Number added...')
  con = str(input('Do you want to continue? [S/N]: ')).strip().upper()[0]
  if con == 'N':
   break
print('=+'*20)
print(f'You typed the values {sorted(lib)}.')