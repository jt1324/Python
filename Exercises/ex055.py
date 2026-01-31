print ('weight')
print ('=+'*10)

lo = 0
hi = 0
for w in range(1, 6):
  wei = float(input("Add the weight of person {}: ".format(w)))
  if w == 1:
    lo = w
    hi = w
  else:
    if wei > hi:
      hi = wei
    if wei < lo:
      lo = wei
  
print ('The higher weight added was {}Kg and the lowest is {}Kg.'.format(hi, lo))