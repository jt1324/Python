from rich import print
from abc import ABC, abstractmethod

class Mother:
    def __init__ (self, name):
        self.name = name

    def make_pizza(self):
        pass

    def fride_eggs(self):
        pass

class Daughter(Mother):
    pass

class Son(Mother):
    pass

