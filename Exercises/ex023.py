num = int(input('Type a number between 0 and 9999: '))
uni = num // 1 % 10
dec = num // 10 % 10
cen = num // 100 % 10
mil = num // 1000 % 10

print ('Unity: {}'.format(uni))
print ('Decimal: {}'.format(dec))
print ('Centena: {}'.format(cen))
print ('Milhar: {}'.format(mil))

# print ('Unity: {:4f}'.format(num[3]))
# print ('Decimal: {:.4f}'.format(num[2]))
# print ('Centena: {:.4f}'.format(num[1]))
# print ('Milhar: {:.4f}'.format(num[0]))