wor = ('learn', 'programming', 'language', 'python', 'course', 'free', 'stydy', 'practice', 'work', 'market', 'programmer', 'future')

vow = 'aeiou'

for w in wor:
  print (f'\nIn the word {w.upper()} there are ', end='' )
  for l in w:
    if l in vow:
      print (f'{l} ', end='')