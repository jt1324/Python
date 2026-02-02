qty = sum = 0

while True:
  num = int(input('Type a number [999 to stop]: '))
  if num == 999:
    break
  qty += 1
  sum += num
print (f'You typed {qty} numbers and the sum is {sum}.')
