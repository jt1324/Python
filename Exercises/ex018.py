import math
ang = int(input('Type the angule you want: '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print('The {} angulo has the SENO of {:.2f}'.format(ang, sen))
print('The {} angulo has the COSSENO of {:.2f}'.format(ang, cos))
print('The {} angulo has the TANGENTE of {:.2f}'.format(ang, tan))