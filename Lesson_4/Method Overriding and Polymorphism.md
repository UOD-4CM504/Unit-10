# Method Overriding and Polymorphism

Method overriding allows a derived (child) class to override a method defined in a base (parent) class.

Polymorphism means "many forms". In computer science, it is often used to mean reusing the same interface (function) for many meanings. In particular, we will be discussing subtyping polymorphism.

## 1. A Simple Example

Let's revisit our animal example from the lesson on inheritance.

This example creates an ``Animal`` class with instance attributes ``name``, ``age``, ``no_legs`` and an instance method ``talk()``.

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


### 1.1 Using Polymorphism

Currently, this does not override the ``talk()`` method in either ``Duck`` or ``Dog``, let's rewrite this so the ``talk()`` method now prints out ``"Woof"`` and ``"Quack"``, respectively. We will remove the ``bark()`` and ``quack()`` methods.

We will also create a list of animals that contain both ``Dog`` instances and ``Duck`` instances, iterate over this list and call the ``talk()`` method. This is polymorphism! 

Why? It is because we know that ``Dog`` and ``Duck`` inherit from ``Animal``, so we know they have a ``talk()`` method. However, we have overridden the method in both derived (child) classes which gives us different behaviour using the same method name, i.e. ``talk()``.

```python
class Animal:
  """ class representing an animal"""
  def __init__(self, name, age, no_legs):
    self.name = name
    self.age = age
    self.no_legs = no_legs

  # override the base talk() method
  def talk(self):
    print(f"Hi I am {self.name}, I am {self.age} years old and I have {self.no_legs} legs")

class Dog(Animal):
  """ class representing a dog"""
  def __init__(self, name, age):
    # here we hardcode the no of legs to be 4
    super().__init__(name, age, 4)

  def talk(self):
    print("Woof")

class Duck(Animal):
  """ class representing a duck"""
  def __init__(self, name, age):
    # here we hardcode the no of legs to be 4
    super().__init__(name, age, 2)

  # override the base talk() method
  def talk(self):
    print("Quack")

if __name__ == "__main__":
  animal_list = []
  dog_one = Dog("Rex", 11)
  duck_one = Duck("Daffy", 84)
  animal_list.append(dog_one)
  animal_list.append(duck_one)
  # because they both inherit from the Animal class we know they have a talk() method
  # this is polymorphism
  for animal in animal_list:
    animal.talk()
```

The last two lines,

```python
  for animal in animal_list:
    animal.talk()
```
show polymorphism in action as we ask two diffent types, ``Dog`` and ``Duck`` to invoke its ``talk()`` method.

The above example now prints out:

```
Woof
Quack
```

## 2. Student and Staff Example

Based on our previous lesson we had the following code to represent a ``Staff`` and a ``Student`` class which inherit from a ``Person`` class.

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

One thing you will notice if you run this code is that both ``Student`` and ``Staff`` instances can invoke (call) the ``send_email()`` method because it is inherited from ``Person``. They can also invoke (call) the methods they define ``is_minor()`` and ``is_pensionable()``. 

Also when we print the instances, e.g. ``print(student_one)`` and ``print(staff_one)``, this is invoking the ``__str__()`` method defined in ``Person``.

### 2.1 Using Polymorphism

However, because ``__str__()`` is defined in ``Person``, when invoked for ``Staff``, it won't print out the national insurance number. We can choose to override this method.

```python
class Staff(Person):
  """ Represents a staff member """

  def __init__(self, first_name, surname, age, staff_id, email, NI_no):
    print("Creating a staff member")
    super().__init__(first_name, surname, age, staff_id, email)
    
    self.NI_no = NI_no

  # override the base __str__ method
  def __str__(self):
    return_string = ""
    return_string += f"Instance of {self.__class__}\n\n"
    return_string += f"Name: {self.first_name} {self.surname}\n"
    return_string += f"Age: {self.age}\n"
    return_string += f"ID: {self.id}\n"
    # also adds NI_no
    return_string += f"National Insurance No.: {self.NI_no}\n"
    return return_string
  
  def is_pensionable(self):
    return self.age >= 65
```

Now when we do ``print(staff_one)`` it will include the national insurance number. Nice.

Except, we are repeating the code. We can again use ``super()`` to simplify this. This time ``super()`` will be used to call the instance method ``__str__()``.

```python
class Staff(Person):
  """ Represents a staff member """

  def __init__(self, first_name, surname, age, staff_id, email, NI_no):
    print("Creating a staff member")
    super().__init__(first_name, surname, age, staff_id, email)
    
    self.NI_no = NI_no

  # override the base __str__ method but use it's functionality via super()
  def __str__(self):
    # call the __str__() method of Person (base) and assign to return_string
    return_string = super().__str__()
    # also adds NI_no
    return_string += f"National Insurance No.: {self.NI_no}\n"
    return return_string
  
  def is_pensionable(self):
    return self.age >= 65
```

We can override any method defined in the base (parent) class. Let's also override the ``send_email()`` method for the ``Staff`` class.

```python
class Staff(Person):
  """ Represents a staff member """

  def __init__(self, first_name, surname, age, staff_id, email, NI_no):
    print("Creating a staff member")
    super().__init__(first_name, surname, age, staff_id, email)
    
    self.NI_no = NI_no

  # override the base __str__ method but use it's functionality via super()
  def __str__(self):
    # call the __str__() method of Person (base) and assign to return_string
    return_string = super().__str__()
    # also adds NI_no
    return_string += f"National Insurance No.: {self.NI_no}\n"
    return return_string
  
  def is_pensionable(self):
    return self.age >= 65

  # override the base send_email method but use it's functionality 
  def send_email(self):
    super().send_email()
    print(f"Staff ID: {self.id}")
```

Our final code looks like this.

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

  def __str__(self):
    # call the __str__() method of Person (base) and assign to return_string
    return_string = super().__str__()
    # also adds NI_no
    return_string += f"National Insurance No.: {self.NI_no}\n"
    return return_string
  
  def is_pensionable(self):
    return self.age >= 65

  def send_email(self):
    super().send_email()
    print(f"Staff ID: {self.id}")

def main():
    student_one = Student("Bradley", "Davis", 25, 87654321, "b.davis@derby.ac.uk")
    student_two = Student("Joe", "Bloggs", 17, 12345678, "j.bloggs@derby.ac.uk")
    staff_one = Staff("Sam", "O'Neill", 38, 12345678, "s.oneill@derby.ac.uk", "ABCDEF123")

    person_list = []
    person_list.append(student_one, student_two, staff_one)

    # polymorphism, we do not know where the __str__() method is implemented, we just know it is.
    for person in person_list:
      print(person)

    # polymorphism, we do not know where the send_email() method is implemented, we just know it is.
    for person in person_list:
      person.send_email()
      
    print(student_one.is_minor())
    print(student_two.is_minor())
    print(staff_one.is_pensionable())

if __name__ == "__main__":
    main()
```

The following lines in the above code demonstrate polymorphism.

```python
    # polymorphism, we do not know where the __str__() method is implemented, we just know it is.
    for person in person_list:
      print(person)

    # polymorphism, we do not know where the send_email() method is implemented, we just know it is.
    for person in person_list:
      person.send_email()
```

That is we know that instances of ``Staff`` and ``Student`` inherit from ``Person`` and therefore have the methods ``__str__()`` and ``send_email()``. However, we have overridden them with gives us different behaviour using the same method name. In fact, we didn't override ``send_email()`` in ``Student``, so it uses the one defined in ``Person``.

## 3. Abstract Classes

An abstract class allows us to template methods that derived classes must implement. 

We can demonstrate this with our earlier animal example. 

Here we make ``Animal`` an abstract class by inheriting the ``ABC`` class (Abstract Base Class).

We can then mark methods as abstract using the decorator ``@abstractmethod``, this forces any derived class such as ``Dog`` to override this method.

```python
from abc import ABC, abstractmethod

class Animal(ABC):
  """ class representing an animal"""
  def __init__(self, name, age, no_legs):
    self.name = name
    self.age = age
    self.no_legs = no_legs

  # abstract method, derived classes must implement!
  @abstractmethod
  def talk(self):
    return 1

class Dog(Animal):
  """ class representing a dog"""
  def __init__(self, name, age):
    # here we hardcode the no of legs to be 4
    super().__init__(name, age, 4)

  def talk(self):
    print("Woof")

class Duck(Animal):
  """ class representing a duck"""
  def __init__(self, name, age):
    # here we hardcode the no of legs to be 4
    super().__init__(name, age, 2)

  # override the base talk() method
  def talk(self):
    print("Quack")

if __name__ == "__main__":
  animal_list = []
  dog_one = Dog("Rex", 11)
  duck_one = Duck("Daffy", 84)
  animal_list.append(dog_one)
  animal_list.append(duck_one)
  # because they both inherit from the Animal class we know they have a talk() method
  # this is polymorphism
  for animal in animal_list:
    animal.talk()
```


The above example will again print out:

```
Woof
Quack
```

Try removing the ``talk()`` method from ``Duck`` and you will get the following error.

```
Traceback (most recent call last):
  File "main.py", line 34, in <module>
    duck_one = Duck("Daffy", 84)
TypeError: Can't instantiate abstract class Duck with abstract method talk
```


# === TASK ===

Create an abstract class called ``Shape``, it should have two abstract methods; ``area()`` and ``perimeter()`` and one attribute ``colour``. 

You should create classes for the following shapes given in the table below. You should inherit from ``Shape`` and override the ``area()`` and ``perimeter()`` methods. **Round both area and circumference to 2 decimal places.**

| Shape | Class Name | Attributes | Area Formula | Perimeter Formula |
| -- | -- | -- | -- | -- |
| Right Triangle | ``RightTriangle`` | ``base``, ``height`` | ``(1/2) * base * height`` | ``base + height + math.sqrt(base**2 + height**2)`` |
| Square | ``Square`` | ``side`` | ``side**2`` | ``4 * side`` |
| Rectangle | ``Rectangle`` | ``base``, ``height`` | ``base * height`` | ``2 * (base + height)`` |

HINT: Remember you will need to use ``self`` to access the instance attributes.

If done correctly you should be able to run this code.

```python
right_tri = RightTriangle(1,1, "Red")
square = Square(1, "Blue")
rectangle = Rectangle(1,2, "Green")

shape_list = []
shape_list.append(right_tri)
shape_list.append(square)
shape_list.append(rectangle)

for shape in shape_list:
  print(shape.area())

print()

for shape in shape_list:
  print(shape.perimeter())

print()

for shape in shape_list:
  print(shape.colour)
```
Which will print out the following.
```
0.5
1
2

3.41
4
6

Red
Blue
Green
```


## Extra Thought

What could ``Square`` inherit from other than ``Shape`` and how would this work?