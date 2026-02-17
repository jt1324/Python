def readInt(msg):
  ok = False
  va = 0
  while True:
    n = str(input(msg))
    if n.isnumeric():
      va = int(n)
      ok = True
    else:
      print ('\033[0;31mERROR! Type a valid number.\033[m')
    if ok:
      break
  return va


n = readInt('Type a number: ')
print(f'You just typed the number {n}')