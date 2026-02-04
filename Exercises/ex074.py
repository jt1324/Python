import random

num = (random.randint(0, 10), random.randint(0, 10), random.randint(0, 10), random.randint(0, 10), random.randint(0, 10))

# option 1 - I have done
print (f'The values are {num}.')
# option 2 - teacher
print ('Os valores sorteados foram:', end='')
for n in num:
  print (f'{n} ', end='')
  
# option 1 - I have done
print (f'The smalest number is {sorted(num)[0]}.')
# option 2 - teacher
print (f'The smalest number is {min(num)}.')

# option 1 - I have done
print (f'\nThe highest number is {sorted(num)[-1]}.')
# option 2 - teacher
print (f'The highest number is {max(num)}.')
