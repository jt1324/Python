numb = (0, 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sisteen', 'seventeen', 'eighteen', 'nineteen', 'twenty')

usu = int(input('Type a number between 1 and 20: '))
while usu not in (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20):
  usu = int(input('Type a number between 1 and 20: '))
pos = numb[usu]
print (f'You typed {pos}')


  