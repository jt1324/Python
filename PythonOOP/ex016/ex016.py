from rich import print

class Cia:
  
  def __init__(self, name, depart, func, comp="Curso em Video"):
    self.name = name
    self.depart = depart
    self.func = func
    self.comp = comp

  def text(self):
    return (f":handshake: Hi, I am [blue]{self.name}[/] and I'm {self.func} from {self.depart} department on company {self.comp}.")

p1 = Cia('Maria', 'Business', 'Director', 'Curso em Video')
print(p1.text())

p2 = Cia('Pedro', 'IT', 'Developer', 'Curso em Video')
print (p2.text())