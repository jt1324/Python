# List []

num = [2, 5, 9, 1]      # list
num[1] = 6              # replace item
num.append(7)           # append item to the end
num.sort()              # sort list
num.sort(reverse=True)  # sort descending
num.insert(2, 0)        # insert item at specific position
num.pop()               # delete last element
num.pop(2)              # delete element from a specific position
num.remove(7)           # remove a specific element (if more than once, will delet the first)
print (num)
print (f'The list has {len(num)} elements.')

print ('=+'*40)

val = []
val.append(5)
val.append(6)
val.append(2)

for v in val:                   # print values only
  print (f'{v}...', end='')

for c, v in enumerate(val):     # print values and postitions
  print (f'\nOn position {c} I found the value {v}.')
print ('I got to the end of the list.')

print ('=+'*40)

lis = []
for cont in range(0, 5):
  lis.append(int(input('Type a value: ')))

for c, v in enumerate(lis):     # print values and postitions
  print (f'On position {c} I found the value {v}.')
print ('I got to the end of the list.')

print ('=+'*40)

a = [2, 3, 4, 7]
b = a                         # this create a connection between the lists
b[2] = 8                      # this will change both lists
c = a[:]                      # this create a copy of list a
c[0] = 1                      # this only changes list c 

print (f'List A: {a}')
print (f'List B: {b}')