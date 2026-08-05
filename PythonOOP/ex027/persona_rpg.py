from abc import abstractmethod
from os import name
from rich import print
import random
from abc import ABC

class Persona(ABC):
    def __init__(self, name, live):
        self.name = name
        self.live = live
        self.blows = []
        # self.target = target
        # self.power = power
        # self.damage = damage
    
    def attack(self, target, power = 100):
        if self.live > 0 and target.live > 0:
            blow = self.blows[random.randrange(0, len(self.blows))]
            print(f"[green]{self.name}[/green]([light_green]{self.live}[/light_green]) attacked [red]{target.name}[/red]([light_green]{target.live}[/light_green]) with a [blue]{blow}[/blue] of power [light_green]{power}[/light_green].") 
        else:
            print(f"The attack {self.name} -> {target.name} can't hapen.")
        


    def take_demage(self, demage):
        dam = random.randint(0, demage)
        self.live = self.live - dam
        if self.live < 0:
            self.vida = 0
        print(f"[blue]{self.name}[/blue] got [red]damage of {dam}[/red]!")


    @abstractmethod
    def heal(self):
        pass


class Warrior(Persona):
    def __init__(self, name, live):
        super().__init__(name, live)
        self.blows = ["Upercut", "Kick", "Hammer Attack"]
    
    def heal(self):
        print(f"[blue]{self.name}[/blue] wrapped a bandage around the wounds and [green]recovered {random.randint(1, 100)} points[/green] of live.")

    
class Wizard(Persona):
    def __init__(self, name, live):
        super().__init__(name, live)
        self.blows = ["Fire Ball", "Tunder Light", "Static Magic"]

    def heal(self):
        print(f"[blue]{self.name}[/blue] worked some healing magic and [green]recovered {random.randint(1, 100)} points[/green] of live.")

