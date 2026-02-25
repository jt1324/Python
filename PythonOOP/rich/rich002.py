from rich import print
from rich.panel import Panel

# Panels


box = Panel("This is an example panel")
print(box)

box1 = Panel("This is an example panel", title="Message", style="green")
print(box1)

box2 = Panel("[white]This is an example panel[/]:+1:", title="Message", style="green", width=30)
print(box2)

