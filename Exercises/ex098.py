from time import sleep

def con(n1, n2, n3):
  print('-='*20)
  if n3 == 0:
    n3 = 1
  if n1 > n2:
    print(f'Counting from {n1} to {n2} in increments of {n3}')
    if n2 <= 0:
      for c in range(n1, n2-1, -n3):
        print(f'{c} ', end=' ', flush=True)
        sleep(0.25)
    else:
      for c in range(n1, n2+1, -n3):
        print(f'{c} ', end=' ', flush=True)
        sleep(0.25)
  else:
    print(f'Counting from {n1} to {n2} in increments of {n3}')
    if n2 <= 0:
      for c in range(n1, n2-1, n3):
        print(f'{c} ', end=' ', flush=True)
        sleep(0.25)
    else:
      for c in range(n1, n2+1, n3):
        print(f'{c} ', end=' ', flush=True)
        sleep(0.25)
  print('FIM!')
  print('-='*20)

con(1 ,10, 1)
con(10, 0, 2)

print("Now it's your time to personilize the counting!")
p1 = int(input('Start: '))
p2 = int(input('End: '))
p3 = int(input('Increments: '))

con(p1, p2, p3)