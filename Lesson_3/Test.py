import pytest
from math import isclose
from main import RegularPolygon, EquilateralTriangle, Square, Pentagon


def test_regular_polygon():
    polygon = RegularPolygon(6, 2)
    assert isclose(polygon.area(), 10.39, rel_tol=1e-2)
    assert polygon.perimeter() == 12.0


def test_equilateral_triangle():
    triangle = EquilateralTriangle(1)
    assert isclose(triangle.area(), 0.43, rel_tol=1e-2)
    assert triangle.perimeter() == 3.0
    assert str(triangle).startswith("EquilateralTriangle")


def test_square():
    square = Square(1)
    assert square.area() == 1.0
    assert square.perimeter() == 4.0
    assert str(square).startswith("Square")


def test_pentagon():
    pentagon = Pentagon(1)
    assert isclose(pentagon.area(), 1.72, rel_tol=1e-2)
    assert pentagon.perimeter() == 5.0
    assert str(pentagon).startswith("Pentagon")


def test_inheritance():
    assert issubclass(EquilateralTriangle, RegularPolygon)
    assert issubclass(Square, RegularPolygon)
    assert issubclass(Pentagon, RegularPolygon)


def test_polymorphism():
    shapes = [EquilateralTriangle(1), Square(1), Pentagon(1)]
    for shape in shapes:
        assert isinstance(shape, RegularPolygon)
        assert hasattr(shape, 'area')
        assert hasattr(shape, 'perimeter')
