from rich import print
from abc import ABC, abstractmethod
from datetime import date

class People(ABC):
    def __init__ (self, name, birth):
        self._name = name
        self._birth = None
        self.birth = birth

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, year:int):
        if year > date.today().year or year < 1900:
            print (f"{year} is not a valid birth year")
        else:
            self._birth = year
            print (f"Birth year changed to {year}")

    @property
    def age(self):
        return date.today().year - self._birth

    @age.setter
    def age(self, value):
        print ("Age can't be changed directly. Change the birth year instead.")


class Student(People):
    official_courses = ["IT", "BUSINESS", "DESIGN", "FINANCE"]
    def __init__ (self, name:str, birth:int, course:str = None):
        super().__init__(name, birth)
        self._course = None
        self.course = course

    @property
    def course(self):
        return self._course

    @course.setter
    def course(self, course:str):
        if course not in self.official_courses:
            print (f"{course} is not an official course")
        else:
            self._course = course
    
    def add_course(self, course:str):
        if course in self.official_courses:
            print (f"{course} is already an official course")
        else:
            self.official_courses.append(course)
            print (f"{course} added to official courses")
