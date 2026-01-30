print('**'*20)
print('Payment Type')
print('--'*20)
pri = int(input('Add the normal price: R$ '))
cho = int(input('Pay in cash = 1, debid card = 2, credit 2x = 3 or credit 3x = 4: '))

if cho == 1:
  print ('For cash payment, the final price is R$ {:.2f}.'.format(pri*0.9))
elif cho == 2:
  print ('For payment in debit card, the final price is R$ {:.2f}.'.format(pri*0.95))
elif cho == 3:
  print ('For payment in 2x on credit card, the price is R$ {:.2f}'.format(pri))
else:
  print ('For payment in 3x on credit card, the price is R$ {:.2f}'.format(pri*1.2))