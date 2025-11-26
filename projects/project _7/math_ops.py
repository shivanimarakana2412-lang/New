import math

def factorial(n):
    """Returns factorial of a number."""
    return math.factorial(n)


def compound_interest(p, r, t):
    """Simple compound interest calculation."""
    return (p * r * t) / 100


def trig_values():
    """Returns trigonometric values in radians."""
    return {
        "sin30": math.sin(math.radians(30)),
        "cos60": math.cos(math.radians(60)),
        "tan45": math.tan(math.radians(45))
    }
