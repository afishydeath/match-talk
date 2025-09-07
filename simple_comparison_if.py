from math import sqrt

x = None
if x == 0:
    pass
elif x == "Hello, Pycon!":
    pass
elif x in (1, 2):
    pass
elif isinstance(x, str):
    pass
elif isinstance(x, tuple) and x == (1, 2, 3, 4):
    pass
elif (
    isinstance(x, list)
    and len(x) >= 2
    and x[:2] == ["python", "is"]
    and (adjectives := x[2:])
):
    pass
elif (
    isinstance(x, list)
    and len(x) == 2
    and x[0] == "twenty"
    and (second_half := x[1]) in ("five", "twentyfive")
):
    pass
elif (
    isinstance(x, dict)
    and "name" in x
    and "greeting" in x
    and (name := x["name"])
    and (greeting := x["greeting"])
):
    rest = x
    rest.pop("name")
    rest.pop("greeting")
    pass
elif isinstance(x, int) and sqrt(x) % 2 == 0:
    pass
else:
    pass
