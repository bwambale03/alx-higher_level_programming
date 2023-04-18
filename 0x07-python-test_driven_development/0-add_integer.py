#!/usr/bin/python3
"""DEfines an Integer addition function"""


def add_integer(a, b=98):
    """
    Return the integre addition of a and b
i
    Float agruments are typecasted to int before addittion is performed

    Raises:
    TypeError: If either a or b is a nonfloat and nont integer value
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an int")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
