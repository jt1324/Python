from rich import print
from abc import ABC, abstractmethod

class People(ABC):
    def __init__ (self, name, birth, course):
        self._name = name
        self._birth = birth
        self.course = course

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
    pass


