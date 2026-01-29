yea = int(input('What year did you born? '))

if (2026-yea) < 18:
  print ('You must enlist to military service in {} years.'.format(18-(2026-yea)))
elif (2026-yea) > 18:
  print ('Your enlist to military service was {} years ago.'.format((2026-yea)-18))
else:
  print ('You must enlist to military service this year.')