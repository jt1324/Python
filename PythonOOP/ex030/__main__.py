from classes030 import *
from rich import print, inspect

def main():
    c = Credentials()
    c.password = "Dunha"

    inspect(c, private=True, methods=True)
    print(c.check("Dunha"))


if __name__ == "__main__":
    main()