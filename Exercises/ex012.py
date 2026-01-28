price = float(input('Add the price: '))
desc = price * ((100-5)/100)
print('The price R$ {} with 5% of dicount is R$ {:.2f}'.format(price, desc))