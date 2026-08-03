from abc import ABC, abstractmethod
from rich import print

class HotDrink(ABC):
    def prepare(self):
        print("--- Starting the preparation ---")
        self.boil()
        self.mix()
        self.serving()
        self.serve()


    def boil(self):
        print("1. Boil the water at 100°C")

    @abstractmethod
    def mix(self):
        pass

    @abstractmethod
    def serving(self):
        pass

    def serve(self):
        print("--- The drink is ready ---")

class Coffee(HotDrink):
    def mix(self):
        print(f"2. Pass the pressured water through the ground coffee powder")

    def serving(self):
        print(f"3. Serve in a small cup")


class Tea(HotDrink):
    def mix(self):
        print(f"2. Put the chosen tea bag in the water and let it brew")

    def serving(self):
        print(f"3. Serve the tea in a porcelain cup with milk and sugar")


class Milk(HotDrink):
    def mix(self):
        print("2. Pass the pressured vapor through the milk")
    
    def serving(self):
        print("3. Serve in a big cup with coffee")