# Sending and Receiving Messages

So far we have had classes that sort of don't interact with each other.

Now we will start to get these classes to combine into a sort of ecosystem of objects that talk to each other.

We will start with a simple example based on the Critter Zoo Program.

We will first create a simple class called ``Critter`` which will contain instance attributes ``name`` and ``no_feed`` (number of times fed), and an instance method ``feed()``.

```python
class Critter:
  """ A very simple critter class"""
  def __init__(self, name):
    self.name = name
    self.no_feeds = 0

  def __str__(self):
    desc = ""
    desc += "Instance of Critter\n"
    desc += f"Name: {self.name}\n"
    desc += f"Fed: {self.no_feeds} times\n"
    return desc

  def feed(self):
    print("Yummy! Thanks! Brruppp...")
    self.no_feeds += 1
```

We will also create a class called ``Caretaker`` which represents a person who looks after critters.

```python
class Caretaker:
  """ A very simple critter class"""
  def __init__(self, name):
    self.name = name

  def __str__(self):
    desc = ""
    desc += "Instance of Caretaker\n"
    desc += f"Name: {self.name}\n"
    return desc

  def feed_criter(self, critter):
    critter.feed()
```

The key method here is ``feed_critter()``, this is now a method that takes in an instance of ``Critter`` and then feeds the little thing by calling the instance method ``feed()``.

You can think about it like this, ``feed_critter()`` takes in a ``Critter`` instance and then sends a message to the ``Critter`` instance by invoking (calling) its method ``feed()``. The ``Critter`` instance in turn receives the message because its method has been invoked, it will then run whatever code is in ``feed()``.

Here is the whole program in action to show you how it works.

```python
class Critter:
  """ A very simple critter class"""
  def __init__(self, name):
    self.name = name
    self.no_feeds = 0

  def __str__(self):
    desc = ""
    desc += "Instance of Critter\n"
    desc += f"Name: {self.name}\n"
    desc += f"Fed: {self.no_feeds} times\n"
    return desc

  def feed(self):
    print("Yummy! Thanks! Brruppp...")
    self.no_feeds += 1

class Caretaker:
  """ A very simple critter class"""
  def __init__(self, name):
    self.name = name

  def __str__(self):
    desc = ""
    desc += "Instance of Caretaker\n"
    desc += f"Name: {self.name}\n"
    return desc

  def feed_criter(self, critter):
    critter.feed()

if __name__ == "__main__":
  alan = Critter("Alan")
  ava = Critter("Ava")
  
  print(alan) # print out alan
  print(ava) # print out ava
  
  bob = Caretaker("Bob")
  bob.feed_criter(alan) # feed alan
  bob.feed_criter(alan) # feed alan
  bob.feed_criter(alan) # feed alan
  bob.feed_criter(ava) # feed ava
  
  print()

  print(alan) # print out alan
  print(ava) # print out ava
  
```
And the output.
```
Instance of Critter
Name: Alan
Fed: 0 times

Instance of Critter
Name: Ava
Fed: 0 times

Yummy! Thanks! Brruppp...
Yummy! Thanks! Brruppp...
Yummy! Thanks! Brruppp...
Yummy! Thanks! Brruppp...

Instance of Critter
Name: Alan
Fed: 3 times

Instance of Critter
Name: Ava
Fed: 1 times
```

We can see that we have asked the instance of ``Caretaker``, ``bob``, to do the feeding. We pass in either ``alan`` or ``ava``, and ``bob`` will feed them by invoking (calling) their ``feed()`` method.

# === TASK ===

Create a ``Plumber`` class and a ``Roomba`` class. 

You might want to look at a [Goomba](https://en.wikipedia.org/wiki/Goomba)...

An instance of ``Plumber`` should be able to squash the ``Roomba``.

The ``Roomba`` class should have an attribute ``name`` and an instance method called ``squish()``. It should also have a non-public attribute ``_squashed`` which should be set to ``False`` when the instance is created (i.e. in the ``__init__()`` method).

Invoking the method ``squish()`` should set ``_squashed`` to ``True``.

You should also override the ``__str__()`` method so that it prints out ``Hi my name is NAME and I am feeling fine`` or ``Hi my name is NAME and I am squashed`` depending on the value of ``_squashed``.

```python
hetti = Roomba("Hetti")
print(hetti) # Hi my name is Hetti and I am feeling fine
hetti.squish() 
print(hetti) # Hi my name is Hetti and I am squashed
```

The ``Plumber`` class should have a ``name`` and an instance method called ``squash()``. 

The ``squash()`` method for the ``Plumber`` class should accept a ``Roomba`` as a parameter. ``squash()`` should then invoke (call) the ``Roomba``'s instance method ``squish()``.

Here is an example of how the two classes should work.

```python
hetti = Roomba("Hetti")
olga = Roomba("Olga")
bob = Roomba("Bob")
print(hetti) # Hi my name is Hetti and I am feeling fine
print(olga) # Hi my name is Olga and I am feeling fine
print(bob) # Hi my name is Bob and I am feeling fine

merio = Plumber("Merio")
merio.squash(olga) # ask merio to squash olga

print(hetti) # Hi my name is Hetti and I am feeling fine
print(olga) # Hi my name is Olga and I am squashed
print(bob) # Hi my name is Bob and I am feeling fine
```
Which would output the following to the console.

```
Hi my name is Hetti and I am feeling fine
Hi my name is Olga and I am feeling fine
Hi my name is Bob and I am feeling fine
Hi my name is Hetti and I am feeling fine
Hi my name is Olga and I am squashed
Hi my name is Bob and I am feeling fine
```


## Getting Started

You can get started by copying and pasting the following into **main.py**.

```python
class Roomba:
  pass

class Plumber:
  pass

def main():
  hetti = Roomba("Hetti")
  olga = Roomba("Olga")
  bob = Roomba("Bob")
  print(hetti) # Hi my name is Hetti and I am feeling fine
  print(olga) # Hi my name is Olga and I am feeling fine
  print(bob) # Hi my name is Bob and I am feeling fine
  
  merio = Plumber("Merio")
  merio.squash(olga)
  
  print(hetti) # Hi my name is Hetti and I am feeling fine
  print(olga) # Hi my name is Olga and I am squashed
  print(bob) # Hi my name is Bob and I am feeling fine

if __name__ == "__main__":
  main()
```