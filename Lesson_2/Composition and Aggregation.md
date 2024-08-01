# Composition and Aggregation 

This lesson briefly introduces the fundamental concept of association in object-oriented programming that allows us to create connections between objects. 

We often refer to classes as composite data types in that they are made up of lots of different data types, whether they are primitive data types like ``int``, ``float``, ``str``, ``bool`` or user-defined data types (classes in Python).

There are two types of associations:

1. Composition
2. Aggregation
   
## 1. Composition

Composition is one of the fundamental concepts of object-oriented programming (OOP). It is often confused with inheritance which we will talk about in the next unit. 

The idea of composition is that you can make up an object from other objects. Think about a car, a car is an object, but it has an engine, it has a gearstick, and it has some seats.

In a sense, the car is now a composition of all these other objects. Those in turn might also be composed of other objects, an engine certainly has many parts.

A good rule of thumb is to say out loud "a car has an engine" and see if it makes sense. Yes, a car does have an engine. If you can say X has a Y, and if Y cannot exist without X, then you should probably use composition. If Y can exist without X, then you probably need aggregation. It is often said to have ownership over the other object.

A good example of this is a room in a house. Here X is the house and Y is the room. Clearly a house has a room but a room cannot exist without the house.

Here we define two classes, an ``Engine`` class which has a ``horse_power`` attribute of type ``int`` and a ``Car`` which has an ``engine`` attribute of type ``Engine``. 

So an instance of ``Car`` is now made up of an instance of another class.

Importantly we pass a ``horse_power`` value to the constructor of ``Car`` and then construct the instance of an ``Engine`` within the ``Car`` instance. Crucially this means that the ``Engine`` instance belongs to the ``Car`` instance, it is said to be tightly coupled. This means if you delete the ``Car`` instance, the ``Engine`` instance is deleted as well.

Here is the example:
```python
class Car:
  def __init__(self, horse_power):
    self.engine = Engine(horse_power)

  def __str__(self):
    return f"A car that has: \n{self.engine}"

class Engine:
  def __init__(self, horse_power):
    self.horse_power = horse_power

  def __str__(self):
    return f"Engine with {self.horse_power} bhp"


if __name__ == "__main__":
  car_one = Car(200)
  print(car_one.engine) # prints Engine with 200 bhp
  print(car_one) 
  # prints
  # A car that has: 
  # Engine with 200 bhp
  del car_one
```

When we run the code, we create an instance of ``Car`` which in turn has a reference to an instance of ``Engine``, you can see this visualised using Python Tutor. When we delete the instance ``car_one``, both are removed from memory.

Before deletion of the ``Car`` instance ``car_one``.

![Before deletion of car_one](assets/composition_1.png)

After deletion of the ``Car`` instance ``car_one``.

![After deletion of car_one](assets/composition_2.png)

## 2. Aggregation

Aggregation is very similar to composition except that the object is not explicitly tied to the instance, it is loosely coupled. 

You can think of it using the object, but not owning it.

Here we pass an instance of an ``Engine`` to the ``Car`` constructor, this will act the same apart from when you delete the instance of the Car, the engine will remain in memory, it exists in its own right!

Which is the right choice depends on the objects and what they represent and how they are associated.

```python
class Car:
  def __init__(self, engine):
    self.engine = engine

  def __str__(self):
    return f"A car that has: \n{self.engine}"

class Engine:
  def __init__(self, horse_power):
    self.horse_power = horse_power

  def __str__(self):
    return f"Engine with {self.horse_power} bhp"


if __name__ == "__main__":
  engine_one = Engine(200)
  car_one = Car(engine_one)
  print(car_one.engine) # prints Engine with 200 bhp
  print(car_one) 
  # prints
  # A car that has: 
  # Engine with 200 bhp
  del car_one
```

Before deletion of the ``Car`` instance ``car_one``.

![Before deletion of car_one](assets/aggregation_1.png)

After deletion of the ``Car`` instance ``car_one``.

![After deletion of car_one](assets/aggregation_2.png)


# === TASK ===

## Student Class
Create a ``Student`` class that has a ``first_name``, ``surname``, ``age``, ``email`` and ``id``.

These can all be public attributes.

Override the ``__str__()`` method so that it prints out the as follows.

```python
student_one = Student("Joe", "Bloggs", 25, "j.bloggs@derby.ac.uk", 12345678)
print(student_one)
```

```
Name: Joe Bloggs
Age: 25
Email: j.bloggs@derby.ac.uk
ID: 12345678
```

## Records Class

Create a ``Records`` class that manages a non-public list of ``_students`` (i.e. a list that will contain instances of ``Student``). 

``Records`` should have two methods:

1. ``add_student()`` that adds an instance of ``Student`` to ``_students``.

```python
records = Records()
student_one = Student("Joe", "Bloggs", 25, "j.bloggs@derby.ac.uk", 12345678)
records.add_student(student_one)
```

2. ``add_students_from_list()`` that takes a list as a parameter and adds this list to the internal list of students ``_students``.

```python
records = Records()
student_one = Student("Joe", "Bloggs", 25, "j.bloggs@derby.ac.uk", 12345678)
student_two = Student("Ada", "Lovelace", 36, "a.lovelace@derby.ac.uk", 87654321)
records.add_student_from_list([student_one, student_two])
```

You should also override the Record ``__str__()`` method so that it prints out each of the students in the student list ``_students`` by using the ``Student`` ``__str__()`` method. 

Instead of accessing the Student ``__str__()`` method directly, you should use the ``str()`` method which will get the value returned from ``__str__()``.

e.g.

```python
student_one = Student("Joe", "Bloggs", 25, "j.bloggs@derby.ac.uk", 12345678)
student_one_str = str(student_one) 
# student_one_str should contain - "Name: Joe Bloggs\nAge: 25\nEmail: j.bloggs@derby.ac.uk\nID: 12345678\n"
print(student_one)
```

```
Name: Joe Bloggs
Age: 25
Email: j.bloggs@derby.ac.uk
ID: 12345678
```
## Some Examples
The below code snippets provide examples of how the classes should operate.

### Adding a Single Student 

```python
records = Records()
student_one = Student("Joe", "Bloggs", 25, "j.bloggs@derby.ac.uk", 12345678)
records.add_student(student_one)
print(records)
```

```
Name: Joe Bloggs
Age: 25
Email: j.bloggs@derby.ac.uk
ID: 12345678
```

### Adding a List of Students

```python
records = Records()
student_one = Student("Joe", "Bloggs", 25, "j.bloggs@derby.ac.uk", 12345678)
student_two = Student("Ada", "Lovelace", 36, "a.lovelace@derby.ac.uk", 87654321)
records.add_student_from_list([student_one, student_two])
print(records)
```

```
Name: Joe Bloggs
Age: 25
Email: j.bloggs@derby.ac.uk
ID: 12345678
Name: Ada Lovelace
Age: 36
Email: a.lovelace@derby.ac.uk
ID: 87654321
```

## Getting Started

You can get started by copying the following into **main.py**

```python
class Student:
  pass


class Records:
  pass


if __name__ == "__main__":
  records = Records()
  student_one = Student("Joe", "Bloggs", 25, "j.bloggs@derby.ac.uk", 12345678)
  student_two = Student("Ada", "Lovelace", 36, "a.lovelace@derby.ac.uk",
                        87654321)
  records.add_student_from_list([student_one, student_two])
  print(records)
```

# References

[Composition and Aggregation in Java](https://www.softwaretestinghelp.com/composition-in-java/)