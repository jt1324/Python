from abc import ABC, abstractmethod #Abstract Base Class

class People(ABC):                                   # Base class | Superclass | Parent class | Class Base | Class Mother
    def __init__(self, name = "", age = 0):
        self.name = name
        self.age = age
    
    def birthday(self):
        self.age += 1

    @abstractmethod
    def study(self):
        pass

class Student(People):                           # Derived class | Subclass | Child class | Class Derived | Class Son
    def __init__ (self, name, age, grade, classroom):
        super().__init__(name, age)
        self.grade = grade
        self.classroom = classroom
    
    def enroll(self):
        print(f"{self.name} is enrolled in {self.classroom} grade {self.grade}")

    def study(self):
        pass


class Teacher(People):                           # Derived class | Subclass | Child class | Class Derived | Class Son
    def __init__(self, name, age, especialty, level):
        super().__init__(name, age)
        self.especialty = especialty
        self.level = level

    def teach(self):
        print(f"{self.name} is teaching {self.especialty} at {self.level} level")
    
    def study(self):
        pass


class Employee(People):                           # Derived class | Subclass | Child class | Class Derived | Class Son  
    def __init__(self, name, age, position, sector):
        super().__init__(name, age)
        self.position = position
        self.sector = sector

    def work(self):
        print(f"{self.name} is working as {self.position} in the {self.sector} sector")

    def study(self):
        pass