#!/usr/bin/python3
""" Square class """


class Square:
    """ Square class parameters """
    def __init__(self, size=0):
        """ Initi a Square
        args:
            size: size of square """
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int) is False:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """  area method """
        return self.__size * self.__size
