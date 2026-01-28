name = input('Type your name: ')
up = name.upper()
mi = name.lower()
le = len(name.strip())-name.count(' ')
fi = name.split()[0]
fil = len(name.split()[0])

print ('Analizing name...')
print ('Your name in capital letters is: {}'.format(up))
print ('Your name in lower letters is: {}'.format(mi))
print ('Your name has {} leters'.format(le))
print ('Your first name is {} and has {} leters'.format(fi, fil))
