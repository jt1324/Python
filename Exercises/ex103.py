def data(p='unknown', g=0):
  print (f'The player {p} scored {g} goals in the championship.')


pla = str(input("Player's name: "))
if pla == '':
  pla = 'unknown'
go = str(input('Goals scored: '))
if go.isnumeric():
  go = int(go)
else:
  go = 0

data(pla, go)