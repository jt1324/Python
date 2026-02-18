info = dict()

def grades(*num, sit=False):
  info['total'] = len (num)
  info['higher'] = max (num)
  info['smaller'] = min (num)
  info['average'] = sum (num)/len (num)
  if sit == True:
    if info['average'] >= 7:
      info['situation'] = 'GOOD'
    elif info['average'] < 5:
      info['situation'] = 'BAD'
    else:
      info['situation'] = 'OK'

res = grades(7.5, 3, 6.5, sit=True)
print (res)
print (info)