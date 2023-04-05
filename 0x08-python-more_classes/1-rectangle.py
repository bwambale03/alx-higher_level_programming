#!/usr/bin/python3
"""
This defines a class - Rectangle
"""


class Rectangle:
    """
    This class has two attributes
    width
    height
    both will have property and setter function definition
    """
    def __init__(self, width=0, height=0):
        """instantiates width and height
        """
        self.width = width
        self.height = height

        @property
        def width(self):
            """
            functin to return width if setter chacks have passed
            """
            return self.__width

        @width.setter
        def width(self, value):
            """
            setter validates if value is >= 0
            Raises:
            TyeError
            ValueError
            """
            if not isinstance(value, int):
                raise TypeError("Width must be an integer")
            if value < 0:
                raise VlueError("width must be >= 0")
            self.__width = value

            @property
            def height(self):
                """
                function to return height if setter checks have passed
                """
                return self.__height

            @height.setter
            def height(self, value):
                """
                setter valuidates if value is >= 0
                Raises:
                TypeError
                ValueError
                """
                if not isinstance(value, int):
                    raise TypeError("value must be an integer")
                if value < 0:
                    raise ValueError("height must be >= 0")
                self.__height = value
