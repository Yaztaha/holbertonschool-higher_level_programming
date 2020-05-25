#!/usr/bin/python3
""" Rectangle module """


class Rectangle:
    """ Rectangle class """

    def __init__(self, width=0, height=0):
        """ Initialization method with width and height """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Rectangle width getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ Rectangle width setter """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ Rectangle height getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ Rectangle height setter """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """ Rectangle area """
        return self.__height * self.__width

    def perimeter(self):
        """ Rectangle perimeter """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width + self.__height) * 2

    def __str__(self):
        """Print rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            boxes = []
            for i in range(self.height):
                boxes += ["#" * self.width]
            return "\n".join(boxes)

    def __repr__(self):
        """ Rectangle string representation """
        return ("Rectangle({:d}, {:d})".format(self.width, self.height))

    def __del__(self):
        """ Rectangle instance deletion """
        print("Bye rectangle...")
