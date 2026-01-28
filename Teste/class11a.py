# STYLE: 0 = none | 1 = bold | 4 = underline | 7 = negative
# TEXT COLOR: 30 = white | 31 = red | 32 = green | 33 = yellow | 34 = blue | 35 = purple | 36 = wather | 37 = grey
# BACKGROUND : 40 = white | 41 = red | 42 = green | 43 = yellow | 44 = blue | 45 = purple | 46 = wather | 47 = grey

# \033[  ;  ;  m  =  \033[style code;text color_code;backgorundm


print('\033[0;30;41mHello World!\033[m')
print('\033[4;33;44mHello World!\033[m')
print('\033[1;35;43mHello World!\033[m')
print('\033[30;42mHello World!\033[m')
print('\033[mHello World!')
print('\033[7;30mHello World!\033[m')

name = str(input('What is your name? '))
print ('Hi {}{}{}, nice to meet you!'.format('\033[4;34m', name, '\033[m'))