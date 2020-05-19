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
        """ getter """
        return self.__size

    @size.setter
    def size(self, value):
        """ size setting
        args:
            value: new value of size """
        if isinstance(value, int) is False:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """  area method of Suqare class """
        return self.size * self.__size

    def my_print(self):
        """ prints in stdout the square with char # """
        for i in range(self.size):
            for j in range(self.size):
                print('#', end='')
            print("")
