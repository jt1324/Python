from classes import *


def main():
    p1 = Mother("Creusa")
    p2 = Daughter("Lisa")
    p3 = Son("Ted")

    p1.make_pizza()
    p1.fride_eggs()

    p2.make_pizza()
    p2.fride_eggs()

    p3.make_pizza()
    p3.fride_eggs()


if __name__ == "__main__":
    main()