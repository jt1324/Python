from rich import print


class Retangule:
    def __init__ (self, base, height):
        self._base = base
        self._height = height
        self._area = None

    @property
    def base(self):
        return self._base
    
    @property
    def height(self):
        return self._height

    @property
    def area (self):
        return self._base * self._height

    def metrics(self, base, height):
        self._base = base
        self._height = height
        self._area = base * height
        print(f"Base = [green]{self._base}[/]\nHeight = [green]{self._height}[/]\nArea = [green]{self._area}[/]")