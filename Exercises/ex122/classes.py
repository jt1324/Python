from rich import print

class Number:
    
    def __init__(self, value: int|float = 0):
        self.value = value

    def fold(self):
        self.value = self.value * 2

    def __str__(self):
        return f"I have the value {self.value} inside the number."


class Text:

    def __init__(self, txt: str = ""):
        self.text = txt

    def fold(self):
        self.text = self.text + " " + self.text

    def __str__(self):
        return f"I have the text '{self.text}' inside the text."


class List:

    def __init__(self, lst:list = []):
        self.values = lst

    def fold(self):
        self.values = self.values + self.values

    def __str__(self):
        return f"I have the list {self.values} inside the list."


class Paper:

    def __init__(self):
        self.folded = False

    def fold(self):
        self.folded = True

    def __str__(self):
        return f"Is the paper folded? {self.folded}."


class House:

    def __init__(self):
        pass

    def __str__(self):
        return f"It's just a house..."


#Duck Typing

def try_fold(object):
    try:
        object.fold()
    except:
        print(f"I had issues trying to folding the {object.__class__.__name__}.")