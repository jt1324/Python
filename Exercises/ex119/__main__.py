from classes import *

def main():
    x = Analyser()
    x.analyse("Python")
    x.analyse(8.5)
    x.analyse(8)
    x.analyse((2, 1, 5))

if __name__ == "__main__":
    main()

