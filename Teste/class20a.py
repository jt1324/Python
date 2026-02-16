a = 4
b = 5
s = a + b
print (s)

a = 8
b = 9
s = a + b
print (s)

a = 2
b = 1
s = a + b
print (s)

def sum(a, b):
  s = a + b
  print(s)


sum(4, 5)
sum(8, 9)
sum(2, 1)

def sum(a, b):
  print(f'A = {a} and B = {b}')
  s = a + b
  print(f'The sum A + B = {s}')

sum(b=4, a=5)


# count paramethers | loop inside def | tuples (not changebles) | desempacotamento
def count(*num):
  for nu in num:
    print(f'One of the values is {nu}.')

def count(*num):
  siz = len(num)
  print(f'I got the values {num} which are {siz} numbers in total.')


count(5, 7, 3, 1, 4)
count(8, 4, 7)


def sum(*valu):
  s = 0
  for numb in valu:
    s += numb
  print(f'The sum of values {valu} is {s}')

sum(5, 2)
sum(2, 9, 4)



# Lists (changeble)

def duble(lst):
  pos = 0
  while pos < len(lst):
    lst[pos]*=2
    pos += 1

values = [6, 3, 9, 1, 0, 2]
duble(values)
print(values)