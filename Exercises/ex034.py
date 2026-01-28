sal = int(input('What is your curent salary? R$'))

if sal >1250:
  print ('Your new salary is R$ {:.2f}.'.format(sal*1.1))
else:
  print ('Your new salary is R$ {:.2f}.'.format(sal*1.15))