print ('Over / Under age')
print ('++'*15)

ove = 0
und = 0
for yea in range(1, 8):
  y = int(input('Add the year of birth: '))
  if (2026 - y) >= 18:
    ove += 1
  else:
    und += 1
print ('From the years added, {} people are over-age and {} are under-age.'.format(ove, und))