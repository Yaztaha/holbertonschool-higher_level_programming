#!/usr/bin/python3
""" Square class """


class Square:
    """ Square class parameters"""
    def __init__(self, size=0):
        """ Init a Square
        args:
            size: size of square """
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    """ area method of Square class """
    def area(self):
        """ area method """
        return self.__size * self.__size
