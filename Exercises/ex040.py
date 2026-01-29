g1 = int(input('Add your first grade: '))
g2 = int(input('Add your second grade: '))
avg = (g1+g2)/2

if avg >= 70:
  print ('APPROVED!')
elif avg < 50:
  print ('FAILED!')
else:
  print ('IN PROCESS.')
