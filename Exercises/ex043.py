hei = float(input('Add your height: '))
wei = float(input('Add your weight: '))
imc = wei/(hei**2)

if imc <18.5:
  print ('Your IMC is {:.2f}, so you are under weight.'.format(imc))
elif imc <=25:
  print ('Your IMC is {:.2f}, so you are in your perfecr weight.'.format(imc))
elif imc <=30:
  print ('Your IMC is {:.2f}, so you are over weight.'.format(imc))
elif imc <=40:
  print ('Your IMC is {:.2f}, so you are obese.'.format(imc))
else:
  print ('Your IMC is {:.2f}, so you are a morbid obese.'.format(imc))