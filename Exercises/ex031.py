dis = int(input('How long is the trip in Km? '))

if dis >200:
  print ('The cost of the trip is R$ {:.2f}'.format(dis*0.45))
else:
  print ('The cost of the trip is R$ {:.2f}'.format(dis*0.5))