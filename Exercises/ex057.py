gen = str(input("Add the person's gender [M/F]: ")).strip().upper()[0]

while gen not in 'MF':
  gen = str(input("Please type only 'M' or 'F': ")).strip().upper()[0]
print ('{} gender added successfuly!'.format(gen))