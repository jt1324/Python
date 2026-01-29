num = int(input('Type a number: '))
cho = int(input('If you want to convert it to binary, type 1, for octal type 2 and for hexa type 3: '))

if cho == 1:
  print ('The binary conversion of {} is {}.'.format(num, bin(num)))
elif cho == 2:
  print ('The octal conversion of {} is {}.'.format(num, oct(num)))
else:
  print ('The hexa conversion of {} is {}.'.format(num, hex(num)))
  