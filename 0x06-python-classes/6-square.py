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
     def position(self, value):
         PosError = "position must be a tuple of 2 positive integers"
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError(PosError)
        if not all(isinstance(val, int) for val in value):
            raise TypeError(PosError)
        if value[0] < 0 or value[1] < 0:
            raise TypeError(PosError)
        self.__position = value

    def area(self):
        """ area method of Square class """
        return self.size * self.size

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
