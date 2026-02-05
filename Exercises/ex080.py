num = []

for n in range(0, 5):
  nu = int(input('Type a number: '))
  if len(num) == 0:
    num.append(nu)
    print ('Added to the list...')
  elif nu > num[-1]:
    num.append(nu)
    print ('Added at the end of the list...')
  else:
    pos = 0
    while pos < len(num):
      if nu <= num[pos]:
        num.insert(pos, nu)
        print(f'Added to position {pos} of the list...')
        break
      pos += 1
print ('=='*15)
print (f'You typed the numbers: {num}.')