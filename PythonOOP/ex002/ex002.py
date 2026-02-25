# declare a class
class MyClass:
  """
  This class create a person witn name and age.
  To create a new person use variable = person(name, age)
  """
  def __init__(self, name = 'unknown', age = 0): # constructor
    # instance attributes
    self.name = name
    self.age = age

  # instance method
  def birthday(self):
    self.age += 1

  # def message(self):
  #   print (f'Hello, my name is {self.name} and I am {self.age} years old.')

  def __str__(self):   # Dunder Method
    return (f'Hello, my name is {self.name} and I am {self.age} years old.')




# declare an object
person = MyClass('Jean', 28)  # create an instance of MyClass and assign it to the variable   person
person.birthday()             # call the birthday method of the person object, which increments the age by 1
# print(person.message()) 

print(person)
# person1 = MyClass('Maria', 30)
# print(person1.message())

# person2 = MyClass()
# print(person2.message())

print(person.__doc__)