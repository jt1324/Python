from rich import print

class Retangule:
    def __init__ (self, base = 1, height = 1):
        self._base = None
        self._height = None
        self._area = None

        self.base = base
        self.height = height

    @property
    def base(self):
        return self._base
    
    @base.setter
    def base(self, value):
        if not isinstance(value, float) and not isinstance(value, int):
            raise TypeError("The base must be a number")
        elif value < 0:
            raise ValueError("The base must be positive")
        else:
            self._base = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, float) and not isinstance(value, int):
            raise TypeError("The height must be a number")
        elif value < 0:
            raise ValueError("The height must be positive")
        else:
            self._height = value


    @property
    def area (self):
        return self._base * self._height

    @area.setter
    def area(self):
        raise PermissionError("You can't change the area of the retangule")

    @property
    def metrics(self):
        return f"Base = [green]{self._base}[/]\nHeight = [green]{self._height}[/]\nArea = [green]{self.area}[/]"

    @metrics.setter
    def metrics(self, values:tuple):
        if not isinstance(values, tuple):
            raise TypeError("The metrics must be a tuple")
        if len(values) != 2:
            raise SyntaxError("The metrics must have 2 values")
        if isinstance(values[0], float) or isinstance(values[0], int):
            self._base = values[0]
        else:
            raise TypeError("The base must be a number")
        if isinstance(values[1], float) or isinstance(values[1], int):
            self._height = values[1]
        else:
            raise TypeError("The height must be a number")