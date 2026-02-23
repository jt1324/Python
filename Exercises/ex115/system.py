from db import *
from time import sleep
from file import file_exist, create_file, read_file, new_reg
from pathlib import Path

fil = Path(__file__).parent / 'data.txt'

if not file_exist(str(fil)):
  create_file(str(fil))

while True:
  sleep(0.75)
  print (header('MAIN MENU'))
  print ('\033[33m1\033[m - \033[34mSee registered people\033[m')
  print ('\033[33m2\033[m - \033[34mRegister new people\033[m')
  print ('\033[33m3\033[m - \033[34mExit\033[m')
  print ('--' * 20)
  opt = readInt('\033[32mYour option:\033[m ')
  if opt == 1:
    read_file(fil)
  elif opt == 2:
    print (header('NEW REGISTER'))
    name = str(input('Name: '))
    age = int(input('Age: '))
    new_reg(fil, name, age)
  elif opt ==3:
    print (header('THANK YOU!'))
    break
  else:
    print ('ERROR! Type a valid option number.')