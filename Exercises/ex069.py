print ('--'*20)
print ('           REGISTER A PERSON')
print ('--'*20)

mal = 0
f20 = 0
ove = 0

while True:
  age = int(input('Age: '))
  gen = str(input('Gender [M/F]: ')).upper().strip()[0]
  while gen not in 'mMfF':
    gen = str(input('Gender [M/F]: ')).strip().upper()[0]
  if gen in 'mM':
    mal += 1
    if age >= 18:
      ove +=1
  else:
    if age >= 18:
      ove += 1
    if age < 20:
      f20 += 1
  con = str(input('Do you want to continue? [Y/N] ')).strip().upper()[0]
  if con in 'nN':
    break
  while con not in 'nNyY':
    con = str(input('Do you want to continue? [Y/N] ')).strip().upper()[0]
print (f'Total of people over age: {ove}.')
print (f'There are {mal} men registered.')
print (f'There are {f20} under 20 years old.')
