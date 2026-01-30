print ('""'*10)
print ('Palindromo')
print ('""'*10)

fra = str(input('Type a frase: ')).strip().upper()
wor = fra.split()
joi = ''.join(wor)

inv = ''
for let in range (len(joi) -1, -1, -1):
  inv += joi[let]

print ('The inverse of {} is {}.'.format(joi, inv))
if inv == joi:
  print ('This is a polindromo!')
else:
  print ('This is not a polindromo!')

