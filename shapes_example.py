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
                return math.pi * self.r**2
            case Rectangle(_, w, h):
                return w * h
            case Shape(side=s):
                return s**2
            case _:
                raise Exception("Unhandled Shape!!")

    def perimiter(self) -> int: ...


class Circle(Shape):
    __match_args__ = ("point", "radius")

    def __init__(self, p: Point, r: int) -> None:
        super().__init__(p)
        self.r: int | float = r


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
    c = Circle(Point(0, 0), 1)
    r = Rectangle(Point(1, 1), 2, 4)
    s = Square(Point(3, 5), 6)
    for i in (c, r, s):
        print(f"{i.area()=}")
