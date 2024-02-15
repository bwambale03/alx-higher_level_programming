#!/usr/bin/python3
"""Defines an Integer addition function"""


def add_integer(a, b=98):
    """
    Return the integer addition of a and b

    Float agruments are typecasted to int before addittion is performed

    Raises:
    TypeError: If either a or b is a nonfloat and nont integer value
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an int")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    if a in[float("inf"), float('-inf')] or b in[float('inf', float('-inf'))]:
        raise OverflowError("cannot convert float infinity to integer")
    if a != a or b != b: # this checks for NaN values
        raise ValueError("cannot convert float NaN to integer")
    return (int(a) + int(b))
