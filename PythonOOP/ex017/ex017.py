from rich import print
from rich.panel import Panel

class Product:

  def __init__(self, name, price):
    self.name = name
    self.price = price

  def stamp(self):
    price_str = f"£{self.price:,.2f}"
    return Panel(f"{self.name.center(40, ' ')}\n{'-' * 40}\n{price_str.center(40, '-')}", title="Product", width=44)
    

p1 = Product ("iPhone 17 Pro Max", 1999.99)
print(p1.stamp())

p2 = Product('Notebook Gamer', 4500.50)
print(p2.stamp())