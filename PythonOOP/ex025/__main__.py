from rich import print
from Transport import *

def main():
    dist = 20

    delivery = Motorcycle(dist)
    print(f"Delivery of {type(delivery).__name__} in {dist} km = {delivery.cost():.2f}")

if __name__ == "__main__":
    main()