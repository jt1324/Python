base = list()
peop = dict()
while True:
  peop.clear()
  peop['name'] = str(input('Name: '))
  while True:
    peop['gender'] = str(input('Gender [M/F]: ')).strip().upper()[0]
    if peop['gender'] in 'MF':
      break
    print('ERROR! Type only M or F.')
  peop['age'] = int(input('Age: '))
  base.append(peop.copy())
  while True:
    con = str(input('Do you want to continue? [Y/N]: ')).strip().upper()[0]
    if con in 'YN':
      break
    print ('ERROR! Please type only Y or N')
  if con == 'N':
    break
print ('=-'*20)
print (f' -The group has {len(base)} people.')
tot = 0
for v in base:
  if tot == 0:
    tot = v['age']
  else:
    tot += v['age']
print (f' -The average age is {tot/len(base):.1f} years.')
print (" -The women registered are: ", end='')
for m in base:
  if m['gender'] == 'F':
    print (f"{m['name']} ", end='')

print ()
print (' -The list of people over the average:')
for o in base:
  if o['age'] > tot/len(base):
    print ('     ')
    for k, v in o.items():
      print (f'{k} {v}; ', end='')
    print ()
print ('=-'*20)
print ('<<FINISHED>>')
  