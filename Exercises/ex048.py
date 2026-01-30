print('**'*8)
print('1 to 500')
print('**'*8)

sum = 0
cou = 0
for c in range(1, 501, 2):
  if c % 3 == 0:
    cou += 1
    sum += c
print('The sum of all the {} values requested is {}.'.format(cou, sum))