from classes028 import *
from rich import print, inspect

def main():
    t = Termostat()
    
    try:
        t.temperature = 25.1
        print(t.ftemperature)
    except Exception as e:
        print(f"There was an error: {e}")

    print(f"The current temperature is [green]{t.ftemperature}[/]")
    inspect(t, private=True, methods=True )

if __name__ == "__main__":
    main()