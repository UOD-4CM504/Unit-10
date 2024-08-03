# main.py
import pytest
from person import *
from io import StringIO
import sys


def test_person_creation():
    person = Person("Alice", 30)
    assert person.name == "Alice"
    assert person.age == 30


def test_person_str_method():
    person = Person("Bob", 25)
    assert str(person) == "Hi I am Bob and I am 25 years old"


def test_say_hello_function(capsys):
    person = Person("Charlie", 40)
    say_hello(person)
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hi I am Charlie and I am 40 years old"


def test_person_with_different_values():
    person1 = Person("David", 18)
    person2 = Person("Eve", 60)

    assert str(person1) == "Hi I am David and I am 18 years old"
    assert str(person2) == "Hi I am Eve and I am 60 years old"


def test_say_hello_with_multiple_people(capsys):
    people = [Person("Frank", 35), Person("Grace", 28)]
    for person in people:
        say_hello(person)

    captured = capsys.readouterr()
    expected_output = "Hi I am Frank and I am 35 years old\nHi I am Grace and I am 28 years old\n"
    assert captured.out == expected_output