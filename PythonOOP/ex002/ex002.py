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

  def __getstate__(self):
    return f"State: Name = {self.name}; Age = {self.age}"



# declare an object
person = MyClass('Jean', 28)  
person.birthday()             
print(person)

print(person.__doc__)
print(person.__dict__)        # Attribute
print(person.__getstate__())  # Method
print(person.__class__)

person1 = MyClass('Maria', 30)
print(person1)
print(person1.__getstate__())