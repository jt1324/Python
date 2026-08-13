from functools import singledispatchmethod

class Analyser:

    @singledispatchmethod
    def analyse(self, value):
        print(f"It wasan't possible to analyse the value {value}")
    
    @analyse.register
    def _(self, value: int):
        print(f"{value} is a int number")

    @analyse.register
    def _(self, value: str):
        print(f"'{value}' is a range of characters")

    @analyse.register
    def _(self, value: float):
        print(f"{value} is a float number")

    @analyse.register
    def _(self, value: tuple|list|dict):
        print(f"{value} is a collection of data")