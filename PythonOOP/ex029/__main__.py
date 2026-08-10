from classes029 import *
from rich import print, inspect


def main():
    d = Diary("Dunha")

    d.write("First message")
    d.write("You're nice")
    d.write("You like Python")

    d.read("Dunha")

    inspect(d, private=True, methods=True)


if __name__ == "__main__":
    main()