from ast import Pass
from rich import print, inspect


class People:                                   # Base class | Superclass | Parent class | Class Base | Class Mother
    def __init__(self, name = "", age = 0):
        self.name = name
        self.age = age
    
    def birthday(self):
        self.age += 1


class Student(People):                           # Derived class | Subclass | Child class | Class Derived | Class Son
    def __init__ (self, name, age, grade, classroom):
        super().__init__(name, age)
        self.grade = grade
        self.classroom = classroom
    
    def enroll(self):
        print(f"{self.name} is enrolled in {self.classroom} grade {self.grade}")


class Teacher(People):                           # Derived class | Subclass | Child class | Class Derived | Class Son
    def __init__(self, name, age, especialty, level):
        super().__init__(name, age)
        self.especialty = especialty
        self.level = level

    def teach(self):
        print(f"{self.name} is teaching {self.especialty} at {self.level} level")


class Employee(People):                           # Derived class | Subclass | Child class | Class Derived | Class Son  
    def __init__(self, name, age, position, sector):
        super().__init__(name, age)
        self.position = position
        self.sector = sector

    def work(self):
        print(f"{self.name} is working as {self.position} in the {self.sector} sector")



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