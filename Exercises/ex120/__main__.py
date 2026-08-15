from classes import *
from rich import print



def main():
    c1 = Wallet(100)
    c2 = Wallet(300)
    
    c1 += 300
    c1 -= 100


    print(c1 == c2)

    print(c1)




if __name__ == "__main__":
    main()