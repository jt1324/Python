from rich import print
from rich.table import Table

table = Table(title="Prices Table")

table.add_column("Name", justify="right", style="green")
table.add_column("Price", justify="center", style="blue")

table.add_row("Pencil", "£ 1.50")
table.add_row("Notebook", "£10.90")
table.add_row("book", "£26.30")

print(table)