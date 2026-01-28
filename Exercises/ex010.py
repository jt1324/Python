amount = int(input('How much Reais do you have? '))
usd = amount/3.27
print('With R$ {} you can buy U$ {:.2f} Dollars'.format(amount, usd))