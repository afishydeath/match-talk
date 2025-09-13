from math import sqrt
from typing import Mapping, Sequence

x = None
if x == 0:
    ...
elif x == "Hello, Pycon!":
    ...
elif x in (1, 2):
    ...
elif isinstance(x, str):
    ...
elif isinstance(x, int) and x == 1:
    ...
elif isinstance(x, float) and x == 1:
    ...
elif isinstance(x, tuple) and x == (1, 2, 3, 4):
    ...
elif (
    isinstance(x, Sequence) and len(x) == 2 and x[0] == ["move"] and (direction := x[1])
):
    ...
elif (
    isinstance(x, Sequence)
    and len(x) >= 2
    and x[:2] == ["python", "is"]
    and (adjectives := x[2:])
):
    ...
elif (
    isinstance(x, Sequence)
    and len(x) == 2
    and x[0] == "twenty"
    and (second_half := x[1]) in ("five", "twentyfive")
):
    ...
elif (
    isinstance(x, Mapping)
    and "name" in x
    and "greeting" in x
    and (name := x["name"])
    and (greeting := x["greeting"])
):
    rest = x
    rest.pop("name")
    rest.pop("greeting")
    ...
elif isinstance(x, int) and sqrt(x) % 2 == 0:
    ...
else:
    ...
