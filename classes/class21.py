# interactive help
# docstrings
# optional parameters
# scope of variables
# return of results from def


# interactive help
help(print)
# help(def)
help(len)

print(input.__doc__)


# docstrings
def cont(s, e, m):
  """
  Docstring for cont
  
  :param s: Start of the counting
  :param e: End of the counting
  :param m: Multiple applied
  :return: no return
  """
  c = s
  while c<= e:
    print(f'{c} ', end='')
    c += m
  print ('END!')

help(cont)


# optional parameters
def sum(a, b=0, c=0): # if there is no parameter, b or c will be 0
  s = a + b + c
  print(f'The sum is {s}.')

sum(3, 2, 5)
sum(3, 2)


# scope of variables
def test():
  n1 = 4
  print(f'N1 inside def is {n1}') # this will be 4

n1 = 2
test()
print (f'N1 outside def is {n1}') # this will be 2


def test2():
  global n2 # this make inside def N2 as global
  n2 = 4
  print(f'N1 inside def is {n2}') # this will be 4

n2 = 2
test()
print (f'N1 outside def is {n2}') # this will be 4


# return of results from def
# no return
def sum (a=0, b=0, c=0):
  s = a + b + c
  print (f'The sum is {s}')

  sum (3, 2, 5)
  sum (2, 7)
  sum (3)

# with return
def sum (a=0, b=0, c=0):
  s = a + b + c
  return s

ret = sum (3, 2, 5)
print (sum (3, 5, 2))

r1 = sum (3, 2, 5)
r2 = sum (2, 7)
r3 = sum (3)
print (f'The sums are {r1}, {r2} and {r3}.')


# exercise
def factor(num = 1):
  f = 1
  for c in range(num, 0, -1):
    f += c
  return f

n = int(input('Add a number: '))
print(f'The factor of {n} is {factor(n)}')

f1 = factor(5)
f2 = factor(4)
f3 = factor()
print(f'The results are {f1}, {f2} and {f3}.')


def even(n=0):
  if n % 2 == 0:
    return True
  else:
    return False

num = int(input('Type a number: '))
if even(num):
  print("It's EVEN!")
else:
  print("It's ODD!")