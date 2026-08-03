from abc import ABC, abstractmethod

class Transport(ABC):
    def __init__(self, distance, cost_per_km):
        self.distance = distance
        self.cost_per_km = cost_per_km

    @abstractmethod
    def cost(self):
        pass

class Motorcycle(Transport):
    def __init__(self, distance):
        super().__init__(distance, 0.5)

    def cost(self):
        return self.distance * self.cost_per_km

class Lorry(Transport):
    def __init__(self, distance):
        super().__init__(distance, 1.2)

    def cost(self):
        if self.distance < 50:
            print("Lorry is not available for distances less than 50 km")
            return 0
        else:
            return self.distance * self.cost_per_km

class Drone(Transport):
    def __init__(self, distance):
        super().__init__(distance, 9.5)

    def cost(self):
        if self.distance > 10:
            print("Drone is not available for distances greater than 10 km")
            return 0
        else:
            return self.distance * self.cost_per_km