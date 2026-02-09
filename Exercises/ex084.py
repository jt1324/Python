na = []
we = []
hea = []
lig = []
hean = []
lign = []
qty = 0


while True:
  n = str(input('Name: ')).strip()
  na.append(n)
  w = int(input('Weight: '))
  we.append(w)
  qty += 1
  c = str(input('Do you want to continue? [Y/N]: ')).strip().upper()[0]
  if qty == 1:
    lig.append(w)
    hea.append(w)
    lign.append(n)
    hean.append(n)
  else:
    if w > hea[0]:
      hea[0] = w
      hean[0] = n
    elif w == hea[0]:
      hea.append(w)
      hean.append(n)
    if w < lig[0]:
      lig[0] = w
      lign[0] = n
    elif w == lig[0]:
      lig.append(w)
      lign.append(n)
  if c == 'N':
    break
print ('=='*20)
print (f'You have registered {qty} people.')
print (f'The heaviest person has {max(we)}Kg. Weight of {hean}.')
print (f'The lightest person has {min(we)}Kg. Weight of {lign}')
