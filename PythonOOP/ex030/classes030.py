import hashlib

class Credentials:
    def __init__(self, password = ""):
        self.__hash = ""
        if password:
            self.password = password

    @property
    def password(self):
        return self.__hash
    
    @password.setter
    def password(self, value):
        self.__hash = hashlib.sha256(value.encode()).hexdigest()

    def check(self, password):
        if self.__hash == hashlib.sha256(password.encode()).hexdigest():
            return f"[green]Password is correct[/]"
        else:
            return f"[red]Password is incorrect[/]"
        