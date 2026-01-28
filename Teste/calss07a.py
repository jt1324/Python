name = input('Your name: ')
print('Nice to meet you {:=^20}!'.format(name))

v1 = int(input('A value: '))
v2 = int(input('Another value: '))
s = v1+v2
m = v1*v2
d = v1/v2
di = v1//v2
e = v1**v2
print('The sum is {}'.format(v1+v2))
print('The sum is {}, \n the multiplication is {} \n and the division is {:.2f}'.format(s, m, d), end='. ')
print('The int division is {} and the potency is {}'. format(di, e))