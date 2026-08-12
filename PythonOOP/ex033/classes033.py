from rich import print
from abc import ABC, abstractmethod

class People(ABC):
    def __init__ (self, name, birth):
        self._name = name
        self._birth = birth

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, birth):
        if birth > 2026:
            print (f"{self._birth} is not a valid birth year")
        elif birth <= 1900:
            print (f"{self._birth} is not a valid birth year")
        else:
            self._birth = birth

    @property
    def age(self):
        return 2026 - self._birth

    @age.setter
    def age(self, value):
        print ("Age can't be changed directly. Change the birth year instead.")


class Student(People):
    def __init__ (self, name, birth, course):
        super().__init__(name, birth)
        self._course = course
        self.official_courses = ["IT", "BUSINESS", "DESIGN", "FINANCE"]

    @property
    def course(self):
        return self._course

    @course.setter
    def course(self, course):
        if course not in self.official_courses:
            print (f"{course} is not a valid course")
        else:
            self._course = course
    
    def add_course(self, course):
        self.official_courses.append(course)
