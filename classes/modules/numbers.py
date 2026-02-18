import useful

num = int(input('Type a number: '))
fat = useful.factor(num)
print (f'The factor of {num} is {fat}.')
print (f'The double of {num} is {useful.doub(num)}')
print (f'The triple of {num} is {useful.trip(num)}')


# ================= OTHER WAY TO DO - NOT RECOMENDED ==================================

from useful import factor, doub, trip

num = int(input('Type a number: '))
fat = factor(num)
print (f'The factor of {num} is {fat}.')
print (f'The double of {num} is {doub(num)}')
print (f'The triple of {num} is {trip(num)}')


# ================= USING PACKAGES ==================================

from useful import numbers

num = int(input('Type a number: '))
fat = numbers.factor(num)
print (f'The factor of {num} is {fat}.')
print (f'The double of {num} is {numbers.doub(num)}')
print (f'The triple of {num} is {numbers.trip(num)}')