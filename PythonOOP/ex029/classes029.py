from rich import print

class Diary:
    def __init__(self, password = ""):
        self.__secrets = []
        self.__password = password

    def write(self, msg = ""):
        self.__secrets.append(msg)

    def read(self, password = ""):
        if self.__password != password:
            print("Incorrect password, you can't read the diary")
        else:
            print(f"[green]Diary is free to read[/]")
            print("\n".join(self.__secrets))
    