from abc import abstractmethod
from rich import print
from random import randint
from abc import ABC

class Persona(ABC):
    def __init__(self, name, live, blow):
        self.name = name
        self.live = live
        self.blow = blow
    
    def attack(self, target, power):
        pass

    def take_demage(self, demage):
        pass

    @abstractmethod
    def heal(self):
        pass


class Warrior():
    def __init__(self):
        pass
    
    def heal(self):
        pass

    
class Wizard():
    def __init__(self):
        pass

    def heal(self):
        pass

