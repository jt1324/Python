from rich import print

class Diary:
    def __init__(self, password = ""):
        self.__secrets = []
        self.__password = password.strip()

    def write(self, msg = ""):
        if isinstance(msg, str) and len(msg.strip()) > 0:
            self.__secrets.append(msg.strip())

    def read(self, password = ""):
        if self.__password != password:
            raise PermissionError("Incorrect password, you can't read the diary")
        else:
            print(f"[green]Diary is free to read[/]")
            print("\n".join(self.__secrets))
    
    @property
    def password(self):
        raise PermissionError("You can't read the password")