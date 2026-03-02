from rich import print

class Pen:
  def __init__(self, color):
    self.color = color
    
  def write(self, text):
    print (f"[{self.color}]{text}[/]")

  def jump(self, lines):
    if lines == 1:
      print('\n')
    else:
      for _ in range(lines-1):
        print('\n')

c1 = Pen('blue')
c2 = Pen('red')
c3 = Pen('green')

c1.write("Hi, are you ok?")
c1.jump(2)
c2.write("Hello mate!")
c2.jump(1)
c3.write("Let's practice!")
