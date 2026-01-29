hou = int(input('What is the price of the house? R$ '))
sal = int(input('What is your monthly salary? R$ '))
per = int(input('For how many years are you planing to pay? '))
mon = hou/(per*12)

print ('The montly payment is R$ {:.2f}.'.format(mon))
if mon >= (sal*0.3):
  print ('Sorry, but the loan was denied as is taking {:.2f}% of your monthly salary'.format(mon/sal))
else:
  print ('Great news, as the montly payment is {:.2f}% of your monthly salary, your loan was approved!'.format(mon/sal))