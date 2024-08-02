import pytest
from main import RightTriangle, Square, Rectangle


def test_right_triangle():
    triangle = RightTriangle(3, 4, "Red")
    assert triangle.area() == 6.0
    assert triangle.perimeter() == 12.0
    assert triangle.colour == "Red"


def test_square():
    square = Square(5, "Blue")
    assert square.area() == 25.0
    assert square.perimeter() == 20.0
    assert square.colour == "Blue"


def test_rectangle():
    rectangle = Rectangle(3, 4, "Green")
    assert rectangle.area() == 12.0
    assert rectangle.perimeter() == 14.0
    assert rectangle.colour == "Green"


def test_shape_polymorphism():
    shapes = [
        RightTriangle(1, 1, "Red"),
        Square(2, "Blue"),
        Rectangle(2, 3, "Green")
    ]
    areas = [shape.area() for shape in shapes]
    perimeters = [shape.perimeter() for shape in shapes]

    assert areas == [0.5, 4.0, 6.0]
    assert perimeters == [3.41, 8.0, 10.0]