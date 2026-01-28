spe = int(input('Add the speed in km/h: '))
pen = (spe-80)*7

if spe >80:
  print ('Your are speeding, your penalty is R$ {:.2f}.'.format(pen))
else:
  print ("Good job, you're respecting the speed limit!")