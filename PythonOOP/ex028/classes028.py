

class Termostat:
    def __init__(self, temperature=24):
        self.__temperature = temperature

    @property
    def temperature(self):
        return self.__temperature

    @temperature.setter
    def temperature(self, value):
        if value < 16 or value > 30:
            print(f"{value} is not a valid temperature")
        else:
            self.__temperature = value



    @property
    def ftemperature(self):
        return f"{self.__temperature}ºC"


