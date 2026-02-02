
qty = 0
max = 0
min = 0
sum = 0
con = 'Y'

while con in 'yY':
  num = int(input('Type a number: '))
  qty += 1
  sum += num
  if qty == 1:
    max = min = num
  else:
    if num > max:
      max = num
    if num < min:
      min = num
  con = str(input('Do you wanto add another number? [Y/N]:')).upper().strip()[0]
print ('You typed {} numbers, the average is {:.2f}, the highest is {} and the lowest is {}.'.format(qty, (sum/qty), max, min))