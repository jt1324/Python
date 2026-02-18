def half(p):
  res = p / 2
  return res

def double(p):
  res = p * 2
  return res

def increase(p, p1, p2):
  res = p + (p*(p1/100))
  return res

def reduce(p, p1, p2):
  res = p - (p*(p2/100))
  return res

# def curr(p, p1, p2):
#   s = (f'£ {p:,.2f}')
#   return s

def summary(p, p1, p2):
  print ('--'*15)
  print ('        VALUE SUMMARY')
  print ('--'*15)
  print (f'price checked:         £{p:.2f}')
  print (f'Half of price:          £{half(p):.2f}')
  print (f'Double of price:       £{double(p):.2f}')
  print (f'Increasing {p1}%:        £{increase(p, p1, p2):.2f}')
  print (f'Reducing {p2}%:           £{reduce(p, p1, p2):.2f}')
  print ('--'*15)