from datetime import datetime

yea = int(input('What year were you born?: '))
def age(n=0):
  ag = datetime.now().year - yea
  return ag

# print (age())

def vote(a):
  if a < 18:
    res = 'denied'
  elif a > 65:
    res = 'Optional'
  else:
    res = 'Mandatory'
  return res

# vote(age())
print(f'With {age()} years your vote is: {vote(age())}')