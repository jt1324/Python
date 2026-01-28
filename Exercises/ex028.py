import random

guess = int(input('Try to guess the nuber I am thinking, between 0 and 5: '))
pc = random.randint(0, 5)

if guess == pc:
  print ('Congrats! you guessed it correct, the number is {}.'.format(pc))
else:
  print ('Sorry, you said {}, but my number is {}.'.format(guess, pc))
print ('Thanks for playing!')