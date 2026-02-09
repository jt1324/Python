mat = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
sum1 = 0

for l in range(0, 3):
  for c in range(0, 3):
    mat[l][c] = int(input(f'Type a value to [{l}, {c}]: '))
print ('=-'*15)
for l in range(0, 3):
  for c in range(0,3):
    print(f'[{mat[l][c]:^5}]', end='')
    if mat[l][c] % 2 == 0:
      sum1 += mat[l][c]
  print()
print ('=-'*15)
print (f'The sum of EVEN values is {sum1}.')
print (f'The sum of the values in the column 3 is {mat[0][2]+mat[1][2]+mat[2][2]}.')
print (f'The highest value on the 2nd line is {max(mat[1])}.')