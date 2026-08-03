from rich import print
from Transport import *
from rich.table import Table

def main():
    distance = 800

    delivery = Lorry(distance)
    print(f"Delivery of {type(delivery).__name__} in {distance} km = {delivery.cost():.2f}")

    table = Table(title="Delivery Costs")
    table.add_column("Transport", justify="center")
    table.add_column("Distance", justify="center")
    table.add_column("Cost", justify="center")
    # table.add_row(type(delivery).__name__, str(distance), f"{delivery.cost():.2f}")
    for TransportType in (Motorcycle, Lorry, Drone):
        delivery = TransportType(distance)
        table.add_row(
            type(delivery).__name__,
            str(distance),
            f"{delivery.cost():.2f}",
        )

    print(table)

if __name__ == "__main__":
    main()