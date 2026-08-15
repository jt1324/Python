from rich import print

class Number:
    
    def __init__(self, value: int|float = 0):
        self.value = value

    def fold(self):
        pass


class Text:

    def __init__(self, txt: str = ""):
        self.text = txt

    def fold(self):
        pass


class List:

    def __init__(self, lst:list = []):
        self.values = lst

    def fold(self):
        pass


class Paper:

    def __init__(self):
        self.folded = False

    def fold(self):
        pass


class House:

    def __init__(self):
        pass

