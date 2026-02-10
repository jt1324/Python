stu = {}

stu['name'] = str(input('Name: '))
stu['grade'] = float(input('Final grade: '))

print (f"Student's name is {stu['name']}")
print (f"The final grade is {stu['grade']}")
if stu['grade'] >= 7:
  print ('The situation is APPROVED')
else:
  print ('The situation is FAILED')