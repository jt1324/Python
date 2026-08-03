from abc import ABC, abstractmethod
import math

class Poligono(ABC):
    def __init__(self, perimeter, area):
        self.perimeter = perimeter
        self.area = area
    
    @abstractmethod
    def qt_sides(self):
        pass


class Square(Poligono):
    def __init__(self, side):
        self.side = side

    def qt_sides(self):
        return 4

    def perimeter(self):
        return 4 * self.side

    def area(self):
        return self.side ** 2


class Circle(Poligono):
    def __init__(self, radius):
        self.radius = radius

    def qt_sides(self):
        return 0

    def perimeter(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * self.radius ** 2



