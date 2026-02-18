test = list()
test.append('Jean')
test.append(46)
group = list()
group.append(test[:])
test[0] = 'Tis'
test[1] = 40
group.append(test[:])
print(group)

print ('--'*30)

people = [['Jhon', 19], ['Deby', 16], ['Ash', 22], ['Callum', 12]]
print (people)
print (people[1][1])

for p in people:
  print (p)
  print (p[0])
  print (p[1])
  print (f'{p[0]} is {p[1]} years old.')

print ('--'*30)

peo = list()
inf = list()

for c in range(0, 3):
  inf.append(str(input('Name: ')))
  inf.append(int(input('Age: ')))
  peo.append(inf[:])
  inf.clear()
print (peo)


und = ove = 0
for p in peo:
  if p[1] < 18:
    print (f'{p[0]} is under aged.')
    und += 1
  else:
    print (f'{p[0]} is over aged.')
    ove += 1

print (f'There are {und} people under age and {ove} over age.')



