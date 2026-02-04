lis = []
for n in range(0, 5):
  lis.append(int(input('Type a number: ')))

# for p, l in enumerate(lis):
print (f'The higest number is: {max(lis)} and is on position {lis.index(max(lis))+1}.')
print (f'The smallest nuber is: {min(lis)} and is on position {lis.index(min(lis))+1}.')
