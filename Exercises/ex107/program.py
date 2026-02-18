import currency

p = float(input('Type a price £'))
print (f'The half of {p} is {currency.half(p):.1f}')
print (f'The double of {p} is {currency.double(p):.1f}')
print (f'Increasing 10%, we have {currency.increase(p):.1f}')
print (f'Reducing 13%, we have {currency.reduce(p):.1f}')