# tuple
food = ('Hamburger', 'juice', 'pizza', 'pudding', 'fries')

print (food)
print (food[0])
print (food[:2])
print (food[3:])
print (food[-1])

for c in food:
  print (f'I will eat {c}.')
print ('I ate a lot!')

for cont in range(0, len(food)):
  print (f'I will eat {food[cont]}.')
print ('I ate a lot!')

for pos, com in enumerate(food):
  print(f'I will eat {com} on position {pos}.')

print(sorted(food))

# ------------------------------------------------------

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print (c)
print(sorted(c))

print(c.count(5)) # how many 5 in the tuple

print(c.index(8)) # find the position os an especific number

# ------------------------------------------------------

person = ('Jean', 46, 'M', 1.74)

print (person)

del(person) # delete whole tuple