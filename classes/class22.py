# errors and exceptions

try:
  a = int(input('NUmber1: '))
  b = int(input('Number2: '))
  r = a / b
except:
  print('Unfortunately we had an issue =(')
else:                                         # opicional
  print (f'The result is {r}')
finally:                                      # opicional
  print ('Thank you!')


# ===== to see details of the error =====

try:
  a = int(input('NUmber1: '))
  b = int(input('Number2: '))
  r = a / b
except Exception as erro:
  print(f'The issue is {erro.__class__}')
else:                                         # opicional
  print (f'The result is {r}')
finally:                                      # opicional
  print ('Thank you!')


# ===== seing details and acting =====

try:
  a = int(input('NUmber1: '))
  b = int(input('Number2: '))
  r = a / b
except (ValueError, TypeError):
  print('The issue is with the data you added.')
except ZeroDivisionError:
  print('Is not possible to divide a number by zero.')
except KeyboardInterrupt:
  print('The user decided not to add the data.')
except Exception as erro:
  print(f'The issue is {erro.__cause__}')
else:                                         # opicional
  print (f'The result is {r}')
finally:                                      # opicional
  print ('Thank you!')