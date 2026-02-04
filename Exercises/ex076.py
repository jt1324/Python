pro = ('Pen', 1.75, 'Ruber', 0.99, 'Notebook', 15.90, 'Pencil', 2.50, 'Ruller', 3.20, 'Bag', 120.32, 'Book', 39.40)

print ('--'*15)
print ('          PRICE LIST')
print ('--'*15)

for p in range (0, len(pro)):
  if p % 2 == 0:
    print (f'{pro[p]:.<20}', end='')
  else:
    print (f'R$ {pro[p]:>7.2f}')
# print (f'{pro[0]}..................R$   {pro[1]}')
# print (f'{pro[2]}................R$   {pro[3]}')
# print (f'{pro[4]}.............R$  {pro[5]:.2f}')
# print (f'{pro[6]}...............R$   {pro[7]:.2f}')
# print (f'{pro[8]}...............R$   {pro[9]:.2f}')
# print (f'{pro[10]}..................R$ {pro[11]}')
# print (f'{pro[12]}.................R$  {pro[13]:.2f}')

print ('--'*15)