from rich import print, inspect
from poligono import *

def main():
    p1 = Circle(20)

    print (f"Perimeter = {p1.perimeter():.1f}")
    print(f"Area = {p1.area():.1f}")


if __name__ == "__main__":
    main()