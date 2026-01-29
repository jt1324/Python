name = str(input('What is your name? '))

if name == 'Jean':
  print ('Such a beautiful name.')
elif name == 'Pedro' or name == 'Maria' or name == 'Paulo':
  print ('Your name is very popular in Brazil.')
elif name in 'Ana claudia Joana Juliana':
  print ('Weird name.')
else:
  print ('Your name is very comum.')
print ('Have a good day!')