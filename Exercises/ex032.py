import calendar

yea = int(input('Add any year: '))

if calendar.isleap(yea):
  print ('The year {} is a leap year.'.format(yea))
else:
  print ('The year {} is not a leap year.'.format(yea))