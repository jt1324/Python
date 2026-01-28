days = int(input('How many days rented? '))
km = float(input('How many Km did you run? '))
value = days*60 + km*0.15
print('The total to pay is R$ {:.2f}'.format(value))
