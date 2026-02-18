from time import sleep

c = ('\033[m',
     '\033[0;30;41m',
     '\033[0;30;42m',
     '\033[0;30;43m',
     '\033[7;30m'
     );

def title(msg, col=0):
  siz = len(msg) + 2
  print (c[col], end='')
  print ('~'*siz)
  print (msg)
  print ('~'*siz)
  print (c[0], end='')

def hel():
  while True:
    title(' HELP SYSTEM PyHELP', 2)
    sub = str(input('  Help subject: '))
    if sub.upper() == 'END':
      break
    sleep(0.5)
    title(f'  Accessing {sub} manual')
    sleep(0.5)
    print (c[4], end='')
    help(sub)
    print (c[0], end='')
  title('  Thank you!', 1)

hel()