from BankAccount import *
from rich import print, inspect

def main():

    a1 = BankAccount(112, 'Jean', 3000, "dunha")
    a1.depo(1500)
    a1.withd(500)
    print(a1)
# print(a1.__doc__)

    # inspect(a1, private=True, methods=True)


if __name__ == "__main__":
    main()