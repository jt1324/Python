people = [
  {'name': 'Ana Paula Santos', 'age': 25},
  {'name': 'Jean Tavares', 'age': 28},
  {'name': 'Maria Silva', 'age': 30},
  {'name': 'João Souza', 'age': 22},
  {'name': 'Carlos Oliveira', 'age': 35},
  {'name': 'Fernanda Lima', 'age': 27},
  {'name': 'Ricardo Pereira', 'age': 31},
  {'name': 'Sofia Costa', 'age': 24},
  {'name': 'Bruno Almeida', 'age': 29},
]

def line(siz=40):
  return '-' * siz

def header(txt):
  print (line())
  print (txt.center(42))
  print (line())

def show():
  # print(header('REGISTERED PEOPLE'))
  for person in people:
    print(f'{person["name"]:<28} {person["age"]:^4} years')

def new():
  # print (header('NEW REGISTER'))
  nam = {}
  # n = str(input('Name: '))
  nam['name'] = n
  # a = int(input('Age: '))
  nam['age'] = a
  people.append(nam)
  print (f'Register of {n} added.')
  
  
def readInt(msg):
  while True:
    try:
      n = int(input(msg))
    except (ValueError, TypeError):
      print ('\033[0;31mERROR! Type a valid number.\033[m')
      continue
    except KeyboardInterrupt:
      print ('\033[0;31mThe user decided not to add the data.\033[m')
      return 0
    else:
      return n
  