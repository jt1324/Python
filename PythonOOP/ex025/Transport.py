from abc import ABC, abstractmethod

class Transport(ABC):
    def __init__(self, distance):
        self.distance = distance
        self.cost_per_km = 0

    @abstractmethod
    def cost(self):
        pass

class Motorcycle(Transport):
    factor = 0.5
    def __init__(self, distance):
        super().__init__(distance)

    def cost(self):
        return self.distance * Motorcycle.factor

class Lorry(Transport):
    factor = 1.2
    def __init__(self, distance):
        super().__init__(distance)

    def cost(self):
        if self.distance < 50:
            print("Lorry is not available for distances less than 50 km")
            return 0
        else:
            return self.distance * Lorry.factor

class Drone(Transport):
    factor = 9.5
    def __init__(self, distance):
        super().__init__(distance)

    def cost(self):
        if self.distance > 10:
            print("Drone is not available for distances greater than 10 km")
            return 0
        else:
            return self.distance * Drone.factor