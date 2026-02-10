# My result -------------------------------------------------------------

# mai = []
# nam = []
# gra = []

# while True:
#   n = str(input('Name: ')).strip()
#   nam.append(n)
#   g1 = float(input('Grade 1: '))
#   gra.append(g1)
#   g2 = float(input('Grade 2: '))
#   gra.append(g2)
#   nam.append(gra)
#   mai.append(nam)
#   gra = []
#   nam = []
#   c = str(input('Do you want to continue? [Y/N]: ')).strip().upper()[0]
#   if c == 'N':
#     break
# print('=-'*20)
# print(f"{'Numb':<6}{'Name':<10}{'Grade Avg':>8}")
# print('--'*15)
# for i, v in enumerate(mai):
#   print (f'{i:<6} {v[0]:<10} {(sum(v[1]))/len(v[1]):>8.1f}')
# print('--'*15)
# while True:
#   n = int(input('Show grades of which student? (999 stops): '))
#   if n == 999:
#     break
#   else:
#     print (f"{mai[n][0]}'s grades are: {mai[n][1]}")
# print ('--  Thank you!  --')

# ======================================================================

# Teacher's result -----------------------------------------------------

lis = list()

while True:
  name = str(input('Name: '))
  grad1 = float(input('Grade 1: '))
  grad2 = float(input('Grade 2: '))
  avg = (grad1 + grad2) / 2
  lis.append([name, [grad1, grad2], avg])
  res = str(input('Continue? [Y/N]: ')).strip().upper()[0]
  if res == 'N':
    break
print('=-'*20)
print(f"{'Numb':<6}{'Name':<10}{'Grade Avg':>8}")
print('--'*15)
for i, a in enumerate(lis):
  print(f'{i:<6}{a[0]:<10}{a[2]:8.1f}')

while True:
  n = int(input('Show grades of which student? (999 stops): '))
  if n == 999:
    break
  else:
    print (f"{mai[n][0]}'s grades are: {mai[n][1]}")
print ('--  Thank you!  --')