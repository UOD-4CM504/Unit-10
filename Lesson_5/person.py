# person.py
# demonstrates having a class and a function in the same module

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"Hi I am {self.name} and I am {self.age} years old"

# simple function that prints out a list of critters
# note this is not in the class Critter
def say_hello(person):
  print(person)