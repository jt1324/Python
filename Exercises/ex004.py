info = input('Type somthing: ')

if info.isnumeric() == True:
  print(f'{info} is nueric')
elif info.isalpha() == True:
  print(f'{info} is alphabetic')
elif info.isalnum() == True:
  print(f'{info} is alpha-numeric')
else:
  print(f'{info} is not numeric, alphabetic or alpha-numeric')