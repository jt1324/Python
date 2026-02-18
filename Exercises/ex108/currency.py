def half(p):
  r = p / 2
  res = (f'£ {r:,.2f}')
  return res

def double(p):
  r = p * 2
  res = (f'£ {r:,.2f}')
  return res

def increase(p):
  r = p + (p*0.1)
  res = (f'£ {r:,.2f}')
  return res

def reduce(p):
  r = p - (p*0.13)
  res = (f'£ {r:,.2f}')
  return res

def curr(p):
  s = (f'£ {p:,.2f}')
  return s