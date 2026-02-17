def data(p='unknown', g=0):
  print (f'The player {p} scored {g} goals in the championship.')


pla = str(input("Player's name: "))
go = str(input('Goals scored: '))
if go.isnumeric():
  go = int(go)
else:
  go = 0
if pla.strip() == '':
  data(g = go)
else:
  data(pla, go)
  
