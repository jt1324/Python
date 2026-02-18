from time import sleep

def hel():
  while True:
    print ('~~'*10)
    print (' HELP SYSTEM PyHELP')
    print ('~~'*10)
    sub = str(input(' Help subject: '))
    if sub == 'end':
      break
    sleep(0.5)
    print ('~~'*12)
    print (f' Accessing {sub} manual')
    print ('~~'*12)
    sleep(0.5)
    help(sub)
  print ('Thank you!')

hel()