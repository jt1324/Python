num = int(input('Type a number: '))
qty = 1
sum = 0

while num != 999:
  sum += num
  qty += 1
  num = int(input('Type another number: '))
print ('You typed {} numbers and the sum of them is {}'.format(qty-1, sum))