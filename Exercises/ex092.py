from datetime import date

data = {}

data['name'] = str(input('Name: '))
data['age'] = date.today().year - int(input('Birthday year: '))
data['NIN'] = int(input("N.I.N. (0 if doesn't have): "))
if data['NIN'] == 0:
  print ('=-'*20)
  print (data)
  print (f'Name is: {data['name']}')
  print (f'The age is: {data['age']}')
  print ("Doesn't have a NIN")
else:
  data['year'] = int(input('Year of start working: '))
  data['salary'] = float(input('Salary: £'))
  print ('=-'*20)
  print (data)
  print (f'Name is: {data['name']}')
  print (f'The age is: {data['age']}')
  print (f'NIN is: {data['NIN']}')
  print (f'Start working year: {data['year']}')
  print (f'The salary is: £{data['salary']}')
  print (f'Will retire at the age {(data['year']+35)-(date.today().year - data['age'])}')
print ('=-'*20)

# --------------

for k, v in data.items():
  print (f' - {k} has the info {v}')