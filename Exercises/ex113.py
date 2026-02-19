def readInt(msg):
  while True:
    try:
      n = int(input(msg))
    except (ValueError, TypeError):
      print ('\033[0;31mERROR! Type a valid number.\033[m')
      continue
    except KeyboardInterrupt:
      print ('\033[0;31mThe user decided not to add the data.\033[m')
      return 0
    else:
      return n

def readFloat(msg):
  while True:
    try:
      n = float(input(msg))
    except (ValueError, TypeError):
      print ('\033[0;31mERROR! Type a valid number.\033[m')
      continue
    except KeyboardInterrupt:
      print ('\033[0;31mThe user decided not to add the data.\033[m')
      return 0
    else:
      return n


n1 = readInt('Type a number: ')
n2 = readFloat('Type a real number: ')
print(f'You just typed the number {n1} and the real number {n2}')