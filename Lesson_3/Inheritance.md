# Inheritance

Let's imagine we were creating a simple university record system that keeps track of both students and staff. 

Consider the following ``class`` that represents a student.

## 1. Student and Staff (No Inheritance)

```python
class Student:
  """ Represents a student """

  def __init__(self, first_name, surname, age, student_id, email):
    self.first_name = first_name
    self.surname = surname
    self.age = age
    self.student_id = student_id
    self.email = email

  def __str__(self):
    return_string = ""
    return_string += "Instance of Student\n\n"
    return_string += f"Name: {self.first_name} {self.surname}\n"
    return_string += f"Age: {self.age}\n"
    return_string += f"ID: {self.student_id}\n"
    return return_string

  def send_email(self):
    print(f"Email sent to {self.email}")

  def is_minor(self):
    return self.age < 18

def main():
    student_one = Student("Bradley", "Davis", 25, 87654321, "b.davis@derby.ac.uk")
    student_two = Student("Joe", "Bloggs", 17, 12345678, "j.bloggs@derby.ac.uk")

    print(student_one)
    print(student_two)
    
    student_one.send_email()
    student_two.send_email()

    print(student_one.is_minor())
    print(student_two.is_minor())

if __name__ == "__main__":
    main()
```

<div style="page-break-after: always;"></div>

We could add another ``class`` that represents a staff member. Add this class to **main.py** and update the ``main()`` method.

```python
class Staff:
  """ Represents a staff member """

  def __init__(self, first_name, surname, age, staff_id, email, NI_no):
    self.first_name = first_name
    self.surname = surname
    self.age = age
    self.staff_id = staff_id
    self.email = email
    self.NI_no = NI_no

  def __str__(self):
    return_string = ""
    return_string += "Instance of Staff\n\n"
    return_string += f"Name: {self.first_name} {self.surname}\n"
    return_string += f"Age: {self.age}\n"
    return_string += f"ID: {self.staff_id}\n"
    return_string += f"NI_no: {self.NI_no}\n"
    return return_string

  def send_email(self):
    print(f"Email sent to {self.email}")

  def is_pensionable(self):
    return self.age >= 65
```

```python
def main():
    student_one = Student("Bradley", "Davis", 25, 87654321, "b.davis@derby.ac.uk")
    student_two = Student("Joe", "Bloggs", 17, 12345678, "j.bloggs@derby.ac.uk")
    staff_one = Staff("Sam", "O'Neill", 38, 12345678, "s.oneill@derby.ac.uk", "ABCDEF123")

    print(student_one)
    print(student_two)
    print(staff_one)
    
    student_one.send_email()
    student_two.send_email()
    staff_one.send_email()

    print(student_one.is_minor())
    print(student_two.is_minor())
    print(staff_one.is_pensionable())

if __name__ == "__main__":
    main()
```

If we look at the ``Student`` and ``Staff`` classes, we will see that they share a lot of characteristics and behaviour. They share a lot of code!

Object orientation tries to deal with this type of code duplication using inheritance. Inheritance is the idea that some classes might have things in common with a base (parent) class. 

Sometimes the derived classes are called child classes. Much like you and I inherit genetics from our parents, you can think of derived (child) classes inheriting from their base (parent) class.

Some simple examples are:

| Base (child) class | Derived (child) class |
| -- | -- |
| ``Shape`` | ``Circle``, ``Square``, ``Triangle`` |
| ``Animal`` | ``Dog``, ``Cat``, ``Cow`` |
| ``Person`` | ``Student``, ``Staff`` |

The last example is exactly what is happening with the above. Both students and staff are people and they all have a name and age. In this case, they also share an email, and university ID and they have an identical method called ``send_email()``. What they don't share is the national insurance number ``NI_no`` and the methods ``is_minor()`` and ``is_pensionable()``.

## 2. Person Class

We will create what is called a base (parent) class that will have all the shared characteristics (attributes) and behaviour (methods). We can then use this to define derived (child) classes that inherit all of these.

```python
class Person:
  """ Represents a person """

  def __init__(self, first_name, surname, age, id, email):
    self.first_name = first_name
    self.surname = surname
    self.age = age
    self.id = id
    self.email = email

  def __str__(self):
    return_string = ""
    return_string += f"Instance of {self.__class__}\n\n"
    return_string += f"Name: {self.first_name} {self.surname}\n"
    return_string += f"Age: {self.age}\n"
    return_string += f"ID: {self.id}\n"
    return return_string

  def send_email(self):
    print(f"Email sent to {self.email}")
```

<div style="page-break-after: always;"></div>

Now we have a person class, the only difference is that it does not have either of the methods ``is_minor()`` or ``is_pensionable()`` and does not have ``NI_no``.

```python
person_one = Person("Bradley", "Davis", 25, 87654321)

# person_one.is_minor() # This will result in an error
# person_one.is_pensionable() # This will result in an error
```

## 3. Updating Student and Staff (with Inheritance)

Now that we have our ``Parent`` class, we can now use this to further define newly derived (child) classes. 

Here are the updated ``Student`` and ``Staff`` classes that inherit from ``Person``.
```python
class Student(Person):
  """ Represents a student """

  def __init__(self, first_name, surname, age, student_id, email):
    # this calls the base (parent) constructor
    super().__init__(first_name, surname, age, student_id, email)

  def is_minor(self):
    return self.age < 18


class Staff(Person):
  """ Represents a staff member """

  def __init__(self, first_name, surname, age, staff_id, email, NI_no):
    # this calls the base (parent) constructor
    super().__init__(first_name, surname, age, staff_id, email)
    self.NI_no = NI_no

  def is_pensionable(self):
    return self.age >= 65
```

As you can see, our ``Student`` and ``Staff`` classes are now much more simple, they inherit from ``Person`` (notice Person is now in paratheses ``()`` e.g. ``class Student(Person)``) and they then define their attributes and methods on top of that.

Also, notice the use of ``super()``. This is a special method that gives the derived (child) class access to the base (parent) class methods. Here we call the base (parent) constructor ``__int__()`` from within the derived (child) classes constructor ``__init__()``.

<div style="page-break-after: always;"></div>

Here is the whole code.

```python
class Person:
  """ Represents a person """

  def __init__(self, first_name, surname, age, id, email):
    print("Person constructor called.")
    self.first_name = first_name
    self.surname = surname
    self.age = age
    self.id = id
    self.email = email

  def __str__(self):
    return_string = ""
    return_string += f"Instance of {self.__class__}\n\n"
    return_string += f"Name: {self.first_name} {self.surname}\n"
    return_string += f"Age: {self.age}\n"
    return_string += f"ID: {self.id}\n"
    return return_string

  def send_email(self):
    print(f"Email sent to {self.email}")

class Student(Person):
  """ Represents a student """

  def __init__(self, first_name, surname, age, student_id, email):
    print("Creating a staff member")
    super().__init__(first_name, surname, age, student_id, email)

  def is_minor(self):
    return self.age < 18


class Staff(Person):
  """ Represents a staff member """

  def __init__(self, first_name, surname, age, staff_id, email, NI_no):
    print("Creating a staff member")
    super().__init__(first_name, surname, age, staff_id, email)
    
    self.NI_no = NI_no

  def is_pensionable(self):
    return self.age >= 65

def main():
    student_one = Student("Bradley", "Davis", 25, 87654321, "b.davis@derby.ac.uk")
    student_two = Student("Joe", "Bloggs", 17, 12345678, "j.bloggs@derby.ac.uk")
    staff_one = Staff("Sam", "O'Neill", 38, 12345678, "s.oneill@derby.ac.uk", "ABCDEF123")

    print(student_one)
    print(student_two)
    print(staff_one)

    student_one.send_email()
    student_two.send_email()
    staff_one.send_email()

    print(student_one.is_minor())
    print(student_two.is_minor())
    print(staff_one.is_pensionable())

if __name__ == "__main__":
    main()
```

The ``Student`` and ``Staff`` classes are now much more concise and only contain the things that are particular to each.

### 3.1 Class Hierarchy

| Class | Inherits From |
| -- | -- |
| ``Person`` | ``object`` Python's base class |
| ``Student`` | ``Person`` |
| ``Staff`` | ``Person`` |

## 4. ``object`` Class

It also turns out that all classes inherit from Python's base class ``object``. To see this we can write this explicitly. Instead of ``class Person:`` we can write ``class Person(object)``. ``object`` has a bunch of things that all classes inherit and can be overridden like ``__init__()``.

```python
class Person(object):
  """ Represents a person """

  def __init__(self, first_name, surname, age, id, email):
    print("Person constructor called.")
    self.first_name = first_name
    self.surname = surname
    self.age = age
    self.id = id
    self.email = email

  def __str__(self):
    return_string = ""
    return_string += f"Instance of {self.__class__}\n\n"
    return_string += f"Name: {self.first_name} {self.surname}\n"
    return_string += f"Age: {self.age}\n"
    return_string += f"ID: {self.id}\n"
    return return_string

  def send_email(self):
    print(f"Email sent to {self.email}")
```

You don't need to write this explicitly, but it is worth knowing.

## 5. Multiple Levels of Inheritance 

It is possible to keep inheriting from classes.

Here we create a slightly different version of ``Person`` but we have a new class ``UniversityMember`` which inherits from ``Person`` and then ``Student`` and ``Staff`` will inherit from ``UniversityMember``.

### 5.1 Class Hierarchy

The following table now summarises the classes, which class they inherit from and their instance attributes and methods.

| ``class`` | Inherits From | Instance Attributes | Instance Methods |
| -- | -- | -- | -- |
| ``Person`` | ``object`` (Python's base class) | ``first_name``, ``surname``,  ``age``, ``home_address`` ||
| ``UniversityMember`` | ``Person`` | ``id``, ``email`` | ``send_email()`` |
| ``Student`` | ``UniversityMember`` | ``uni_address`` | ``is_minor()`` |
| ``Staff`` | ``UniversityMember`` | ``NI_no`` | ``is_pensionable()`` |

### 5.2 Implementaion

Here is our new code that implements this class hierarchy. Copy and paste this into **main.py** to see it working.

```python
class Person:
  """ Represents a person """

  def __init__(self, first_name, surname, age, home_address):
    self.first_name = first_name
    self.surname = surname
    self.age = age
    self.home_address = home_address
  def __str__(self):
    return_string = ""
    return_string += f"Instance of {self.__class__}\n\n"
    return_string += f"Name: {self.first_name} {self.surname}\n"
    return_string += f"Age: {self.age}\n"
    return_string += f"Address: {self.home_address}\n"
    return return_string

  def send_email(self):
    print(f"Email sent to {self.email}")

class UniversityMember(Person):
  """ Represents a University Member"""
  def __init__(self, first_name, surname, age, home_address, student_id, email):
    super().__init__(first_name, surname, age, home_address)
    self.id = id
    self.email = email

class Student(UniversityMember):
  """ Represents a student """

  def __init__(self, first_name, surname, age, home_address, uni_address, student_id, email):
    super().__init__(first_name, surname, age, home_address, student_id, email)
    self.uni_address = uni_address

  def is_minor(self):
    return self.age < 18


class Staff(UniversityMember):
  """ Represents a staff member """

  def __init__(self, first_name, surname, age, home_address, staff_id, email, NI_no):
    super().__init__(first_name, surname, age, home_address, staff_id, email)
    
    self.NI_no = NI_no

  def is_pensionable(self):
    return self.age >= 65

def main():
    student_one = Student("Bradley", "Davis", 25, "Somewhere he calls home", "XR lab, he sleeps here", 87654321, "b.davis@derby.ac.uk",)
    student_two = Student("Joe", "Bloggs", 17, "Home sweet home", "Uni digs", 12345678, "j.bloggs@derby.ac.uk")
    staff_one = Staff("Sam", "O'Neill", 38, "His house", 12345678, "s.oneill@derby.ac.uk", "ABCDEF123")

    print(student_one)
    print(student_two)
    print(staff_one)

    student_one.send_email()
    student_two.send_email()
    staff_one.send_email()

    print(student_one.is_minor())
    print(student_two.is_minor())
    print(staff_one.is_pensionable())

if __name__ == "__main__":
    main()
```

## 6. A Simple Animal Example

The following example creates an ``Animal`` class with instance attributes ``name``, ``age``, ``no_legs`` and an instance method ``talk()``.

We then inherit from ``Animal`` to create a ``Dog`` and a ``Duck`` class.

Notice that when we call ``super().__init__()`` in the ``Dog`` and ``Duck`` constructor (``__init__()``) we hardcode the ``no_legs`` to ``4`` and ``2``, respectively. 

Why bother asking the person creating the instance of ``Dog`` or ``Duck`` the number of legs when you know the answer?

Here is the code.

```python
class Animal:
  """ class representing an animal"""
  def __init__(self, name, age, no_legs):
    self.name = name
    self.age = age
    self.no_legs = no_legs

  def talk(self):
    print(f"Hi I am {self.name}, I am {self.age} years old and I have {self.no_legs} legs")

class Dog(Animal):
  """ class representing a dog"""
  def __init__(self, name, age):
    # here we hardcode the no of legs to be 4
    super().__init__(name, age, 4)

  def bark(self):
    print("Woof")

class Duck(Animal):
  """ class representing a duck"""
  def __init__(self, name, age):
    # here we hardcode the no of legs to be 4
    super().__init__(name, age, 2)

  def quack(self):
    print("Quack")

if __name__ == "__main__":
  animal_list = []
  dog_one = Dog("Rex", 11)
  duck_one = Duck("Daffy", 84)
  animal_list.append(dog_one)
  animal_list.append(duck_one)
  # because they both inherit from the Animal class we know they have a talk() method
  for animal in animal_list:
    animal.talk()

  # however they have their own instance methods bark() and ``quack``

  dog_one.bark()
  duck_one.quack()
```

This will print out:

```
Hi I am Rex, I am 11 years old and I have 4 legs
Hi I am Daffy, I am 84 years old and I have 2 legs
Woof
Quack
```

We will see a better way to do this using polymorphism in a later lesson.

# === TASK ===

*Please note that we could probably do this **TASK** differently and there are arguments for that, however, it is a simple exercise to help test inheritance.*

Create a ``RegularPolygon`` class that has an attributes ``no_sides``, ``side_length`` and instance methods ``area()`` and ``perimeter()``.

You can compute the area and perimeter of a regular polygon as follows. 

**You should compute the area and perimeter to 2 decimal places.**

### Area of A Regular Polygon

``AREA = (1/4)*no_sides * (side_length**2 / math.tan(math.pi/no_sides))``

Note that you will need the ``math`` module to use ``pi`` and ``tan``.

### Perimeter of A Regular Polygon

``PERIMETER = no_sides * side_length``

[Maths is Fun - Regular Polygons](https://www.mathsisfun.com/geometry/regular-polygons.html#:~:text=A%20%22Regular%20Polygon%22%20has%3A,all%20angles%20equal.)

## Extending RegularPolygon


Extend the ``RegularPolygon`` class to create ``EquilateralTriangle``, ``Square`` and ``Pentagon``. Each class should correctly set ``no_sides`` to ``3``, ``4`` and ``5``, respectively.

Implement the ``__str__()`` method so that it returns the following string.

| ``class`` | ``__str()__`` returns |
| -- | -- |
| ``EquilateralTriangle`` | ``"EquilateralTriangle\n\nArea: {AREA}\n\nPerimeter: {PERIMETER}\n"`` |
| ``Square`` | ``"Square\n\nArea: {AREA}\n\nPerimeter: {PERIMETER}\n"`` |
| ``Pentagon`` | ``"Pentagon\n\nArea: {AREA}\n\nPerimeter: {PERIMETER}\n"`` |

### Equilateral Triangle Example

```python
tri = EquilateralTriangle(1)
print(tri)
```
Prints out:
```
EquilateralTriangle

Area: 0.43

Perimeter: 3
```

### Square Example

```python
square = Square(1)
print(square)
```
Prints out:
```
Square

Area: 1.0

Perimeter: 4
```

### Pentagon Example

```python
pent = Pentagon(1)
print(pent)
```
Prints out:
```
Pentagon

Area: 1.72

Perimeter: 5
```

You can generate more examples using [Calculator Soup - Regular Polygon Calculator](https://www.calculatorsoup.com/calculators/geometry-plane/polygon.php).

## Getting Started 

You can get started by copying and pasting the following into **main.py**.

```python
import math

class RegularPolygon:
  pass

class EquilateralTriangle(RegularPolygon):
  pass
  
class Square(RegularPolygon):
  pass

class Pentagon(RegularPolygon):
  pass

if __name__ == "__main__":
  tri = EquilateralTriangle(1)
  square = Square(1)
  pent = Pentagon(1)

  print(tri)
  print(square)
  print(pent)
```

# References

[Maths is Fun - Regular Polygons](https://www.mathsisfun.com/geometry/regular-polygons.html#:~:text=A%20%22Regular%20Polygon%22%20has%3A,all%20angles%20equal.)

[Calculator Soup - Regular Polygon Calculator](https://www.calculatorsoup.com/calculators/geometry-plane/polygon.php)