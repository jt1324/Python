print ('--'*15)
print ('Multiplication table')
print ('--'*15)


while True:
  print('--'*40)
  num = int(input('DO you want to see the multiplication table of what number? '))
  print (f'{num} x 1 = {num* 1}')
  print (f'{num} x 1 = {num* 2}')
  print (f'{num} x 1 = {num* 3}')
  print (f'{num} x 1 = {num* 4}')
  print (f'{num} x 1 = {num* 5}')
  print (f'{num} x 1 = {num* 6}')
  print (f'{num} x 1 = {num* 7}')
  print (f'{num} x 1 = {num* 8}')
  print (f'{num} x 1 = {num* 9}')
  print (f'{num} x 1 = {num*10}')
  if num <0:
    break
print ('Finished, thank you!')
