from abc import ABC, abstractmethod
import math

class Poligono(ABC):
    def __init__(self, qty_sides):
        self.qty_sides = qty_sides
        
    
    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass


class Square(Poligono):
    def __init__(self, side = 1):
        super().__init__(4)
        self.side = side

    def perimeter(self):
        return self.side * 4

    def area(self):
        return self.side ** 2


class Circle(Poligono):
    def __init__(self, radius = 1):
        super().__init__(0)
        self.radius = radius

    def perimeter(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * self.radius ** 2



