mai = [[], []]
c = 1

for n in range (0, 7):
  num = int(input(f'Add the {c} number: '))
  c += 1
  if num % 2 == 0:
    mai[0].append(num)
  else:
    mai[1].append(num)
print ('++'*20)
mai.sort
print (f'The EVEN numbers are: {sorted(mai[0])}.')
print (f'The ODD numbers are: {sorted(mai[1])}.')
print (f'The full list is: {sorted(mai[0])}{sorted(mai[1])}.')

# --------


# mai = []
# eve = []
# odd = []
# c = 1

# for n in range (0, 7):
#   num = int(input(f'Add the {c} number: '))
#   c += 1
#   if num % 2 == 0:
#     eve.append(num)
#   else:
#     odd.append(num)
# mai.append(sorted(eve))
# mai.append(sorted(odd))
# print ('++'*20)
# print (f'The EVEN numbers are: {eve}.')
# print (f'The ODD numbers are: {odd}.')
# print (f'The full list is: {mai}.')




