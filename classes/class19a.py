# Dictionary  -  similar to hash

# Tuple ()
# List []
# Dictionary {}

data = dict()
data = {'name':'Pedro','age':25 }
print (data['name']) # Pedro
print (data['age'])  # 25

data['gender']='M'   # create new field (no append)

del data['age']      # delete field

movie = {
  'title':'Star Wars',
  'year':1977,
  'director':'George Lucas'
}

print (movie.values())   # Star Wars, 1977, Geoge Lucas
print (movie.keys())     # title, year, director
print (movie.items())     # title: Star Wars, year: 1977, director: George Lucas

for k, v in movie.items():
  print(f'The {k} is {v}.')   # The title is Star Wars.
                              # The year is 1977.
                              # The director is George Lucas.

people = {'name': 'Gustavo', 'gender': 'M', 'age': 22}
print(f"{people['name']} is {people['age']} year old.")
people['weight'] = 90                                    # Add a new field
people['name'] = 'Lucas'                                 # Amend field's value
for k, v in people.items():
  print(f'{k} = {v}')

# Dictionari inside a list

brazil = []
state1 = {'uf': 'Rio de Janeiro', 'abrev': 'RJ'}
state2 = {'uf': 'Sao paulo', 'abrev': 'SP'}
brazil.append(state1)
brazil.append(state2)

print (brazil)             # [{'uf': 'Rio de Janeiro', 'abrev': 'RJ'}, {'uf': 'Sao paulo', 'abrev': 'SP'}]  
print (brazil[0])          # {'uf': 'Rio de Janeiro', 'abrev': 'RJ'}
print (brazil[1])          # {'uf': 'Sao paulo', 'abrev': 'SP'}
print (brazil[0]['uf'])    # Rio de Janeiro
print (brazil[1]['abrev']) # SP


#-------------------------------------------------------------------------

sta = dict()
bra = list()
for c in range(0, 3):
  sta['uf'] = str(input('State name: '))
  sta['abrev'] = str(input('Abrev of the state: '))
  bra.append(sta.copy())
print (bra)               # if don't use copy() = [{'uf': 'Minas Gerais', 'abrev': 'MG'}, {'uf': 'Minas Gerais', 'abrev': 'MG'}, {'uf': 'Minas Gerais', 'abrev': 'MG'}]
for e in bra:
  for k, v in e.items():
    print(f'The field {k} has the value {v}.')