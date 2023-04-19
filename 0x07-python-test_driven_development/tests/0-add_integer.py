#!/usr/bin/python3
"""Defines and integer addition function"""


def add_integer(a, b=98):
    """
    Return the integere addition of a and b


    Float agruments are typecasted to an int before addition is performed

    Raises:
    TypeError:If of either a or b is non-integer and non-float
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
