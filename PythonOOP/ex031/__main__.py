from Retangule import *
from rich import print, inspect

def main():
    r = Retangule(8,-4)

    inspect(r)

    r.metrics(9, 3)

    print(r.metrics)


if __name__ == "__main__":
    main()