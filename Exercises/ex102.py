def fact(n, show=False):
  """
  Docstring for fact
  
  :param n: Start of factorial calculation
  :param show: Show or not the details of the calculation
  :return: The value of factorial n
  """
  f = 1
  for c in range(n, 0, -1):
    if show:
      print(f'{c} x ',end='')
    f *= c
  return f

print(fact(5, show=True))
print(fact(5))