from rich import print
from rich.panel import Panel
from rich.traceback import install
install()


class Check:
  weight_per_person = 0.4
  price_per_kg = 25.00

  def __init__(self, title, qty):
    self.title = title
    self.qty = qty

  def bbq(self):
    return Panel(f"Checking [green]{self.title}[/] with [blue]{self.qty} people[/]\nEach person will eat {self.weight_per_person}Kg and the Kg cost is £{self.price_per_kg:,.2f}\nRecomended buy [blue]{self.qty * self.weight_per_person}[/]Kg of meat\nThe total cost will be [green]£{((self.qty * self.weight_per_person) * self.price_per_kg):,.2f}[/]\nEach person will pay [yellow]£{(((self.qty * self.weight_per_person) * self.price_per_kg) / self.qty):,.2f}[/] to join.", title=f'{self.title}')
  

bbq1 = Check('Friends BBQ', 50)
print(bbq1.bbq())