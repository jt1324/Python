# # MY SOLUTION
# l1 = [[], [], []]
# l2 = [[], [], []]
# l3 = [[], [], []]

# n1 = 0
# n2 = 0

# for n in range (1, 10):
#   if n < 4:
#     num = int(input(f'Type a value to [{n1}, {n2}]: '))
#     l1[n2].append(num)
#     n2 += 1
#     if n == 3:
#       n2 = 0
#   elif n < 7:
#     n1 = 1
#     num = int(input(f'Type a value to [{n1}, {n2}]: '))
#     l2[n2].append(num)
#     n2 += 1
#     if n == 6:
#       n2 = 0
#   else:
#     n1 = 2
#     num = int(input(f'Type a value to [{n1}, {n2}]: '))
#     l3[n2].append(num)
#     n2 += 1
# print ('-='*20)
# print (f'{l1[0]} {l1[1]} {l1[2]}')
# print (f'{l2[0]} {l2[1]} {l2[2]}')
# print (f'{l3[0]} {l3[1]} {l3[2]}')


# TEACHER'S SOLUTION

mat = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(0, 3):
  for c in range(0, 3):
    mat[l][c] = int(input(f'Type a value to [{l}, {c}]: '))
print ('=-'*15)
for l in range(0, 3):
  for c in range(0,3):
    print(f'[{mat[l][c]:^5}]', end='')
  print()