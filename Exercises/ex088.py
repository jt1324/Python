import random

print ('--'*15)
print ('      EURO MILLION GAME')
print ('--'*15)

pla = int(input('How many times do you want to play? '))
c = 1

print (f"{'-='*5}  Getting numbers for {pla} games  {'=-'*5}")

for r in range(0, pla):
  num = (random.randint(0, 60), random.randint(0, 60), random.randint(0, 60), random.randint(0, 60), random.randint(0, 60), random.randint(0, 60))
  print(f'Game {c} : {num}')
  c += 1
print (f"{'=='*5} < GOOD LUCK > {'=='*5}")