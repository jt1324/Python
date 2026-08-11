from BankAccount import *
from rich import print, inspect

def main():

    a1 = BankAccount(112, 'Jean', 3000)
    a1.depo(1500)
    a1.withd(500)
    print(a1)
    
    # inspect(a1, private=True, methods=True)


if __name__ == "__main__":
    main()