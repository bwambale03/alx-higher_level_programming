#!/usr/bin/python3
"""
Defines a function that prints a name
"""


def say_my_name(first_name, last_name=""):
    """print a name

    Args:
    first_name(str): the first name to print.
    last_name(str): The last name to print.
    Raises:
    TypeError: If either first-name or second_name are strings
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TyoeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))