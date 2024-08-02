from abc import ABC, abstractmethod
import math


class Shape(ABC):

    def __init__(self, colour):
        self.colour = colour

    # you can leave these blank
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class RightTriangle(Shape):
    def __init__(self, base, height, colour):
        super().__init__(colour)
        self.base = base
        self.height = height

    def area(self):
        return round((1 / 2) * self.base * self.height, 2)

    def perimeter(self):
        return round(self.base + self.height + math.sqrt(self.base ** 2 + self.height ** 2), 2)


class Square(Shape):
    def __init__(self, side, colour):
        super().__init__(colour)
        self.side = side

    def area(self):
        return round(self.side ** 2, 2)

    def perimeter(self):
        return round(4 * self.side, 2)


class Rectangle(Shape):
    def __init__(self, base, height, colour):
        super().__init__(colour)
        self.base = base
        self.height = height

    def area(self):
        return round(self.base * self.height, 2)

    def perimeter(self):
        return round(2 * (self.base + self.height), 2)


if __name__ == "__main__":
    right_tri = RightTriangle(1, 2, "Red")
    square = Square(1, "Blue")
    rectangle = Rectangle(1, 2, "Green")

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