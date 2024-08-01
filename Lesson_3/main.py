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