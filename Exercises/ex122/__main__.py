from classes import *
from rich import print


def main():
    a = Number(200)
    b = Text("Python")
    c = List([1, 2, 3])
    d = Paper()
    e = House()

    try_fold(a)
    try_fold(b)
    try_fold(c)
    try_fold(d)
    try_fold(e)


    print(a)
    print(b)
    print(c)
    print(d)
    print(e)




if __name__ == "__main__":
    main()