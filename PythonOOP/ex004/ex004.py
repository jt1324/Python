from ast import Pass


class People:                                   # Base class | Superclass | Parent class | Class Base | Class Mother
    def __init__(self, name = "", age = 0):
        self.name = name
        self.age = age
    
    def birthday(self):
        self.age += 1


class Student(People):                           # Derived class | Subclass | Child class | Class Derived | Class Son
    def __init__ (self, name, age, grade, classroom):
        super().__init__(name, age)
        self.grade = ""
        self.classroom = ""
    
    def enroll(self):
        pass


class Teacher(People):                           # Derived class | Subclass | Child class | Class Derived | Class Son
    def __init__(self, name, age, especialty, level):
        super().__init__(name, age)
        self.especialty = ""
        self.level = ""

    def teach(self):
        pass


class Employee(People):                           # Derived class | Subclass | Child class | Class Derived | Class Son  
    def __init__(self, name, age, position, sector):
        super().__init__(name, age)
        self.position = ""
        self.sector = ""

    def work(self):
        pass