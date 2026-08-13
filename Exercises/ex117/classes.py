

class Animal:
    def __init__(self, make_sound):
        self.make_sound = make_sound


class Cat(Animal):
    def __init__(self, make_sound):
        super().__init__(make_sound)

class Dog(Animal):
    def __init__ (self, make_sound):
        super().__init__(make_sound)

class Chicken(Animal):
    def __init__ (self, make_sound):
        super().__init__(make_sound)

class Duck(Animal):
    def __init__ (self, make_sound):
        super().__init__(make_sound)