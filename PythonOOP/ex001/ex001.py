# declare a class
class MyClass:
  def __init__(self): # constructor
    # instance attributes
    self.name = ''
    self.age = 0

  # instance method
  def birthday(self):
    self.age += 1

  def message(self):
    print (f'Hello, my name is {self.name} and I am {self.age} years old.')



# declare an object
person = MyClass()        # create an instance of MyClass and assign it to the variable person
person.name = 'Jean'      # set the name attribute of the person object to 'Jean'
person.age = 28           # set the age attribute of the person object to 28
person.birthday()         # call the birthday method of the person object, which increments the age by 1
print(person.message())   # call the message method of the person object, which prints a message with the name and age of the person

person1 = MyClass()
person1.name = 'Maria'
person1.age = 30
print(person1.message())