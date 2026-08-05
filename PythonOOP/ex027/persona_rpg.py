from abc import abstractmethod
from rich import print
from random import randint
from abc import ABC

class Persona(ABC):
    def __init__(self, name, live, blow = 0, target, power, damage):
        self.name = name
        self.live = live
        self.blow = randint(1, self.power)
        self.target = target
        self.power = power
        self.damage = damage
    
    def attack(self, target, power):
        print(f"[green]{Warrior(self.name)}[/green]([light_green]{self.live}[/light_green]) attacked 
            [red]{Wizard(self.name)}[/red]([light_green]{Wizard(self.live)}[]/light_green) with a [blue]Upercut[/blue] of power 
            [light_green]{self.power}[/light_green].") 
        print(f"[blue]{Wizard(self.name)}[/blue] got [red]damage of {dem}[/red]!")


    def take_demage(self, demage):
        dem = randint(1, self.demage)


    @abstractmethod
    def heal(self):
        pass


class Warrior():
    def __init__(self):
        pass
    
    def heal(self):
        print(f"[blue]{self.name}[/blue] wrapped a bandage around the wounds and [green]recovered {randint(1, 100)} points[/green] of live.")

    
class Wizard():
    def __init__(self):
        pass

    def heal(self):
        print(f"[blue]{self.name}[/blue] worked some healing magic and [green]recovered {randint(1, 100)} points[/green] of live.")

