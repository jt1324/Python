def lin(l):
  while l > 0:
    print('-', end='')
    l -= 1

tex = str(input('Write a text: '))
w = int(len(tex)+4)

lin(w)
print()
print (f'  {tex}')
lin(w)
