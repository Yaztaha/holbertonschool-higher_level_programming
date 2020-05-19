#!/usr/bin/python3
""" Square class """


class Square:
    """ Square class parameters """
    def __init__(self, size=0, position=(0, 0)):
        """ Init a Square
        args:
            size: size of square """
        self.size = size
        self.position = position

    @property
    def size(self):
        """ Getter """
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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        PosError = "position must be a tuple of 2 positive integers"
        if type(position) is not tuple and len(position) is not 2:
            if position[0] < 0 and position[1] < 0:
                raise TypeError(PosError)
        self.__position = position

    def area(self):
        """ area method of Square class """
        return self.size * self.__size

    def my_print(self):
        """ prints to stdout a square in char # """
        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            for k in range(self.__position[0]):
                print(" ", end="")
            for j in range(self.__size):
                print('#', end='')
            print("")
        if self.size == 0:
            print()
