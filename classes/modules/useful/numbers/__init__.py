def factor(n):
  f = 1
  for c in range(1, n+1):
    f *= c
  return f

def doub(n):
  return n * 2

def trip(n):
  return n * 3