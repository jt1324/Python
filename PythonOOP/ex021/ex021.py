from rich import print

class Pen:
  def __init__(self, color, cover=False):
    self.color = color
    self.cover = False
    
  def uncover(self):
    self.cover = True
  
  def write(self, text):
    if self.cover == True:
      print (f"[{self.color}]{text}[/]")
    else:
      print (f"The [{self.color}]pen[/] is covered!")
  
  def jump(self, lines):
    if lines == 1:
      print('\n')
    else:
      for _ in range(lines-1):
        print('\n')


c1 = Pen('blue')
c2 = Pen('red')
c3 = Pen('green')

c1.uncover()
c2.uncover()
# c3.uncover()

c1.write("Hi, are you ok?")
c1.jump(2)
c2.write("Hello mate!")
c2.jump(1)
c3.write("Let's practice!")
