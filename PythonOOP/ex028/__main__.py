from classes028 import *
from rich import print, inspect

def main():
    t = Termostat()
    t.temperature = 27.2
    print(f"The current temperature is [green]{t.temperature}[/]")
    inspect(t, private=True, methods=True )

if __name__ == "__main__":
    main()