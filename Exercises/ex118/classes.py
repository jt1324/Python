from rich import print
from abc import ABC, abstractmethod

class Mother:
    def __init__ (self, name):
        self.name = name

    def make_pizza(self):
        print(f"{self.name} is making a margerita PIZZA.")

    def fride_eggs(self):
        print(f"{self.name} is frying 1 EGG.")

class Daughter(Mother):
    def make_pizza(self):
        print(f"{self.name} is making a Tunna PIZZA.")
    
    def fride_eggs(self):
        print(f"{self.name} is frying 2 EEGs.")

class Son(Mother):
    def make_pizza(self):
        print(f"{self.name} is making a four-cheese PIZZA.")

    def fride_eggs(self):
        print(f"{self.name} is frying 4 EGGs.")

