from ast import Pass
from rich import print, inspect

from class_ex_005 import Student, Teacher, Employee




s1 = Student("John", 20, "IT", "1A")
s1.birthday()
s1.enroll()
inspect(s1, methods=True)

t1 = Teacher("Jane", 30, "Math", "Master")
t1.birthday()
t1.teach()
inspect(t1, methods=True)

e1 = Employee("Jim", 40, "Manager", "HR")
e1.birthday()
e1.work()
inspect(e1, methods=True)