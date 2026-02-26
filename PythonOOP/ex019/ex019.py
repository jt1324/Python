from time import sleep
from rich import print

class Book:

  def __init__(self, title, pages):
    self.title = title
    self.pages = pages
    self.current_page = 1
    print (f":book: You just opened the book '[red]{self.title}[/]' which has [green]{self.pages} pages[/] in total. You are now on [yellow]page 1[/]")

  
  def pass_pages(self, pas):
    if self.current_page == 1:
      rang = pas
    elif self.current_page + pas > self.pages:
      rang = self.pages - self.current_page
    else:
      rang = pas
    for _ in range(rang):
      self.current_page += 1
      print (f"Pg{self.current_page} :arrow_forward:  ", end='')
      sleep(0.35)
    print (f"[blue]You passed {rang} pages and is now on page[/] [yellow]{self.current_page}[/]")
    if self.current_page >= self.pages:
      print(f":blue_book: [red]You got to the end of the book {self.title}.[/]")
      

b1 = Book("10 thinkg I've learned", 20)
b1.pass_pages(5)
b1.pass_pages(10)
b1.pass_pages(10)
