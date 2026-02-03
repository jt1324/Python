print ('__'*10)
print ('    PYTHON BANK')
print ('TT'*10)

c50 = 0
c20 = 0
c10 = 0
c01 = 0
res = 0

while True:
  wit = int(input('How much do you want to withdraw? R$ '))
  res = wit
  if wit >= 50:
    while res >= 50:
      c50 += 1
      res -= 50
  if res == 0:
    break
  if res >= 20:
    while res >= 20:
      c20 += 1
      res -= 20
  if res == 0:
    break
  if res >= 10:
    while res >= 10:
      c10 += 1
      res -= 10
  if res == 0:
    break
  if res >= 1:
    while res >= 1:
      c01 += 1
      res -= 1
  if res == 0:
    break
print (f'Total of {c50} cels of R$ 50.00')
print (f'Total of {c20} cels of R$ 20.00')
print (f'Total of {c10} cels of R$ 10.00')
print (f'Total of {c01} cels of R$ 1.00')
print ('=='*30)
print ('Hope you see you back soon to Python Bank! Have a good day!')
print ('=='*30)