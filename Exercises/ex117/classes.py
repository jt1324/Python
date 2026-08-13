from rich import print
from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name:str):
        self.name = name

    @abstractmethod
    def make_sound(self):
        print(f"{self.name} is a {self.__class__.__name__} and is making a sound")

class Cat(Animal):
    def make_sound(self):
        print(f"{self.name} is making a meow sound")

class Dog(Animal):
    def make_sound(self):
        print(f"{self.name} is making a bark sound")


class Chicken(Animal):
    def make_sound(self):
        print(f"{self.name} is making a cluck sound")

class Duck(Animal):
    def make_sound(self):
        print(f"{self.name} is making a quack sound")