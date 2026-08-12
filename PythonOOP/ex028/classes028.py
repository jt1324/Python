

class Termostat:
    def __init__(self):
        self.__temperature = 24
        # self.temperature = temperature

    @property
    def temperature(self):
        return self.__temperature

    @temperature.setter
    def temperature(self, value):
        if value < 16:
            self.__temperature = 16
        elif value > 30:
            self.__temperature = 30
        elif value % 0.5 != 0:
            raise ValueError(f"{value}{chr(176)}C is not a valid temperature (use whole numbers or .5)")
        else:
            self.__temperature = value


    @property
    def ftemperature(self):
        return f"{self.__temperature}{chr(176)}C"


