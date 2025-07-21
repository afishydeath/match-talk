# an example for the extended use of match statements for a fraction class
NUMS = "⁰¹²³⁴⁵⁶⁷⁸⁹"
DENS = "₀₁₂₃₄₅₆₇₈₉"


class Fraction:
    __match_args__ = ("numerator", "denomenator")

    def __init__(self, numerator: int, denomenator: int):
        self.numerator = numerator
        self.denomenator = denomenator


def print_fraction(frac: Fraction | int) -> str:
    match frac:
        case int():
            return str(frac)
        case Fraction(_, 0):
            return "NaN"
        case Fraction(0, _):
            return "0"
        case Fraction(n, 1):
            return str(n)
        case Fraction(n, d) if n == d:
            return "1"
        case Fraction(n, d) if (n < 0 and d > 0) or (n > 0 and d < 0):
            return "-" + print_fraction(Fraction(abs(n), abs(d)))
        case Fraction(n, d) if n > d:
            return str(n // d) + print_fraction(Fraction(n % d, d))
        case Fraction(n, d):
            return NUMS[n] + "/" + DENS[d]
        case _:
            raise Exception("frac was not matched")


if __name__ == "__main__":
    while i := input("> "):
        n, d = map(int, i.split("/"))
        print(print_fraction(Fraction(n, d)))
