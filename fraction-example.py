# an example for the extended use of match statements for a fraction class
import math

NUMS = "⁰¹²³⁴⁵⁶⁷⁸⁹"
DENS = "₀₁₂₃₄₅₆₇₈₉"


def format_script(script: str, number: int) -> str:
    return "".join([script[int(x)] for x in str(number)])


class Fraction:
    __match_args__ = ("numerator", "denominator")

    def __init__(self, n: int, d: int):
        self.numerator = n
        self.denominator = d
        self.valid = d != 0


def print_fraction(frac: Fraction) -> str:
    match frac:
        case Fraction(valid=False):
            return "NaN"
        case Fraction(0, _):
            return "0"
        case Fraction(n, 1):
            return str(n)
        case Fraction(n, d) if n == d:
            return "1"
        case Fraction(n, d) if n < 0 and d < 0:
            return print_fraction(Fraction(-n, -d))
        case Fraction(n, d) if n < 0 or d < 0:
            return "-" + print_fraction(Fraction(abs(n), abs(d)))
        case Fraction(n, d) if n > d:
            return str(n // d) + print_fraction(Fraction(n % d, d))
        case Fraction(n, d) if (g := math.gcd(n, d)) > 1:
            return print_fraction(Fraction(n // g, d // g))
        case Fraction(n, d):
            return format_script(NUMS, n) + "/" + format_script(DENS, d)
        case _:
            raise Exception("frac was not matched")


if __name__ == "__main__":
    while i := input("> "):
        n, d = map(int, i.split("/"))
        print(print_fraction(Fraction(n, d)))
