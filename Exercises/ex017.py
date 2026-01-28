import math
op = float(input('Width of the cateto oposto: '))
ad = float(input('Width of the cateto adjacente: '))
hip = (op ** 2 + ad **2) ** (1/2)
hi_math = math.hypot(op, ad)
print('The hipotenusa will be {:.2f}'.format(hip))
print('The hipotenusa will be {:.2f}'.format(hi_math))