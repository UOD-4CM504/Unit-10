# Modules and Classes

This is a fairly straightforward lesson.

Basically, you can create modules which contain both functions and classes. 

A module should contain related code, whether that be in the form of functions or classes.

For example, we could create a ``Critter`` class and also create a function called ``print_critter_list()``.

Here are the contents of ``critter.py``.

```python
# critter.py
# demonstrates having a class and a function in the same module

class Critter:
  def __init__(self, name):
    self.name = name

  def __str__(self):
    return f"Hi I am {self.name}"

# simple function that prints out a list of critters
# note this is not in the class Critter
def print_critter_list(critter_list):
  for critter in critter_list:
    print(critter)
```
Here are the contents of **main.py**.

```python
# main.py
from critter import Critter, print_critter_list

# create a list of critters using the imported Critter class
critter_list =[Critter("Bob"), Critter("Sue"), Critter("Ava"), Critter("Alan")]

# print the list of critters using the imported print_critter_list function
print_critter_list(critter_list)
```

Running **main.py** will print out the following:

```
Hi I am Bob
Hi I am Sue
Hi I am Ava
Hi I am Alan
```


If you are interested in how to structure larger projects you can search on the internet and you will find lots of best practices and tutorials.

However, it is out of the scope of this course.

# === TASK ===

Create a module called ``person.py``. It should contain a single class ``Person`` and a single function ``say_hello()``.

The class ``Person`` should have attributes ``name`` and ``age`` and you should override the ``__str__()`` method so that it returns ``Hi I am NAME and I am AGE years old``.

The function ``say_hello()`` should take in an instance of ``Person`` and print out the instance of ``Person``.

You can copy the following into ``main.py`` to get started, but you will need to have the ``Person`` class and ``say_hello`` function set up in ``hello.py``.
```python
# main.py
from person import Person, say_hello
terry = Person("Terry", 45)
say_hello(terry)
```

Which will print out:

```
Hi I am Terry and I am 45 years old
```