import math


class RegularPolygon:
    def __init__(self, no_sides, side_length):
        self.no_sides = no_sides
        self.side_length = side_length

    def area(self):
        return round((1 / 4) * self.no_sides * (self.side_length ** 2 / math.tan(math.pi / self.no_sides)), 2)

    def perimeter(self):
        return round(self.no_sides * self.side_length, 2)


class EquilateralTriangle(RegularPolygon):
    def __init__(self, side_length):
        super().__init__(3, side_length)

    # we could do this with polymorphism, not introduced yet
    def __str__(self):
        return_string = "EquilateralTriangle\n\n"
        return_string += f"Area: {self.area()}\n\n"
        return_string += f"Perimeter: {self.perimeter()}\n"
        return return_string


class Square(RegularPolygon):
    def __init__(self, side_length):
        super().__init__(4, side_length)

    # we could do this with polymorphism, not introduced yet
    def __str__(self):
        return_string = "Square\n\n"
        return_string += f"Area: {self.area()}\n\n"
        return_string += f"Perimeter: {self.perimeter()}\n"
        return return_string


class Pentagon(RegularPolygon):
    def __init__(self, side_length):
        super().__init__(5, side_length)

    # we could do this with polymorphism, not introduced yet
    def __str__(self):
        return_string = "Pentagon\n\n"
        return_string += f"Area: {self.area()}\n\n"
        return_string += f"Perimeter: {self.perimeter()}\n"
        return return_string


if __name__ == "__main__":
    tri = EquilateralTriangle(1)
    square = Square(1)
    pent = Pentagon(1)

    print(tri)
    print(square)
    print(pent)
    print(type(pent).__bases__[0])
