from classes028 import *
from rich import print, inspect

def main():
    t = Termostat()
    # t.temperature = 25
    # print(f"The current temperature is {t.ftemperature}")
    inspect(t, private=True, methods=True )

if __name__ == "__main__":
    main()