from db import *

def file_exist(name):
  try:
    a = open(name, 'rt')
    a.close()
  except FileNotFoundError:
    return False
  else:
    return True
  
  
def create_file(name):
  try:
    a = open(name, 'wt+')
    a.close()
  except:
    print ('There was an ERROR when creating the file')
  else:
    print (f'File {name} create succesfully!')

def read_file(name):
  try:
    a = open(name, 'rt')
  except:
    print ('Erro reading the file')
  else:
    header('REGISTERED PEOPLE')
    # print(a.read())
    for person in a:
      dat = person.split(';')
      dat[1] = dat[1].replace('\n', '')
      print(f'{dat[0]:<29} {dat[1]:^4} years') 
  finally:
    a.close()


def new_reg(fil, name='unknown', age=0):
  try:
    a = open(fil, 'at')
  except:
    print ('Erro opening the file')
  else:
    try:    
      a.write(f'{name};{age}\n')
    except:
      print ('ERROR when wrinting the info')
    else:
      print (f'Register of {name} added.')
      a.close()