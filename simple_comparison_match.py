from math import sqrt

x = None
match x:
    case 0:
        pass
    case "Hello, Pycon":
        pass
    case 1 | 2:
        pass
    case str():
        pass
    case tuple((1, 2, 3, 4)):
        pass
    case ["python", "is", *adjectives]:
        pass
    case ["twenty", ("five" | "twentyfive") as second_half]:
        pass
    case {"name": name, "greeting": greeting, **rest}:
        pass
    case int(x) if sqrt(x) % 2 == 0:
        pass
    case _:
        pass
