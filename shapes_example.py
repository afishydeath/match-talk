import math


class Point:
    __match_args__ = ("x", "y")

    def __init__(self, xpos: int, ypos: int):
        self.x: int | float = xpos
        self.y: int | float = ypos


class Shape:
    __match_args__ = ("point",)

    def __init__(self, p: Point) -> None:
        self.point = p

    def area(self) -> int | float:
        match self:
            case Circle():
                return math.pi * self.radius**2

            case Shape(side=s):
                return s**2

            case Rectangle(_, w, h):
                return w * h

            case _:
                raise Exception("Unhandled Shape!!")

    def contains_point(self, point: Point) -> bool:
        match self:
            case Circle(Point(x, y), r):
                return (point.x - x) ** 2 + (point.y - y) ** 2 <= r**2

            case Square(p, s):
                return Rectangle(p, s, s).contains_point(point)

            case Rectangle(Point(x, y), w, h) if (
                point.x >= x and point.x <= x + w and point.y >= y and point.y <= y + h
            ):
                return True
            case Rectangle():
                return False
            case _:
                raise Exception("Unhandled Shape!")


class Circle(Shape):
    __match_args__ = ("point", "radius")

    def __init__(self, p: Point, r: int | float) -> None:
        super().__init__(p)
        self.radius: int | float = r


class Rectangle(Shape):
    __match_args__ = ("point", "width", "height")

    def __init__(self, p: Point, w: int | float, h: int | float) -> None:
        super().__init__(p)
        self.width: int | float = w
        self.height: int | float = h


class Square(Rectangle):
    __match_args__ = ("topleft", "side")

    def __init__(self, p: Point, s: int):
        super().__init__(p, s, s)
        self.side = s


if __name__ == "__main__":
    testc = Circle(Point(0, 0), 2)
    testr = Rectangle(Point(1, 1), 2, 4)
    tests = Square(Point(3, 5), 6)
    testp = Point(1, 1)
    for i in (testc, testr, tests):
        print(f"{i.area()=} {i.contains_point(testp)=}")
