from ex008 import BankAccount

def main():
    c1 = BankAccount(111, "Mary", 5000)
    c1.depo(-500)
    c1.withd(-100)
    c1.__balance = 0

    print(c1)

if __name__ == "__main__":
    main()