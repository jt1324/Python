time = int(input('How old is your car?' ))
if time <= 3:
  print("New car")
else:
  print("Old car")
print ('-- END --')

print ('New car' if time <=3 else 'Old car')


name = str(input('Your name? '))
if name == 'Jean':
  print ('Such a bealtiful name!')
print ('Good morning {}!'.format(name))
