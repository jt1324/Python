from rich import print


class Door:
    def open(self):
        print("turn the door holder and pull | push")


class Company:
    def open(self):
        print("Get the documentation to set up a company")


class Egg:
    def open(self):
        print("Break the shell")


class Rock:
    pass


# Pythonic Polymorphic method Duck Typing

def try_open(object):
    try:
        object.open()
    except:
        print(f"I found issues when trying to open the {object.__class__.__name__}")