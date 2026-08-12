from classes033 import *
from rich import print, inspect


def main():
    a1 = Student("Dunha", 2009, "IT")

    a1.birth = 2010
    # a1.age = 15
    a1.add_course("MEDICINE")
    a1.course = "MEDICINE"

    inspect(a1, private=True, methods=True)
    

if __name__ == "__main__":
    main()