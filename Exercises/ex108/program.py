import currency

p = float(input('Type a price £'))
print (f'The half of {currency.curr(p)} is {currency.half(p)}')
print (f'The double of {currency.curr(p)} is {currency.double(p)}')
print (f'Increasing 10%, we have {currency.increase(p)}')
print (f'Reducing 13%, we have {currency.reduce(p)}')