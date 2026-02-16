print ('Land control')
print('--'*15)

# lan = list()

w = float(input('Width (m): '))
# lan.append(wid)
l = float(input('Length (m): '))
# lan.append(leng)

def data(wid, leng):
  s = wid * leng
  print(f'The area of the land {wid}x{leng} is {s:.2f} square meters')

data(w, l)