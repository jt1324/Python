from rich import print
from rich.panel import Panel
from rich.traceback import install
install()


class Check:

  def __init__(self, title, qty):
    self.title = title
    self.qty = qty

  def bbq(self):
    return Panel(f"Checking [green]{self.title}[/] with [blue]{self.qty} people[/]\nEach person will eat 0.4Kg and the Kg cost is £25.00\nRecomended buy [blue]{self.qty * 0.4}[/]Kg of meat\nThe total cost will be [green]£{(self.qty * 0.4)*25:,.2f}[/]\nEach person will pay [yellow]£{((self.qty * 0.4)*25)/self.qty:,.2f}[/] to join.", title=f'{self.title}')
  

bbq1 = Check('Friends BBQ', 50)
print(bbq1.bbq())