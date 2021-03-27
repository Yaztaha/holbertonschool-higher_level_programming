#!/usr/bin/python3
"""Module containing Rectangle class"""

from models.base import Base


class Rectangle(Base):
    """Rectangle Class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Init method for Rectangle class"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter method for width"""

        return self.__width

    @width.setter
    def width(self, value):
        """Validator setter method for width"""

        if type(value) is not int:
            raise(TypeError("width must be an integer"))
        if value <= 0:
            raise(ValueError("width must be > 0"))
        self.__width = value

    @property
    def height(self):
        """Getter method for height"""

        return self.__height

    @height.setter
    def height(self, value):
        """Validator setter method for height"""

        if type(value) is not int:
            raise(TypeError("height must be an integer"))
        if value <= 0:
            raise(ValueError("height must be > 0"))
        self.__height = value

    @property
    def x(self):
        """Getter method for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Validator setter method for x"""

        if type(value) is not int:
            raise(TypeError("x must be an integer"))
        if value < 0:
            raise(ValueError("x must be >= 0"))
        self.__x = value

    @property
    def y(self):
        """Getter method for y"""

        return self.__y

    @y.setter
    def y(self, value):
        """Validator setter method for y"""

        if type(value) is not int:
            raise(TypeError("y must be an integer"))
        if value < 0:
            raise(ValueError("y must be >= 0"))
        self.__y = value

    def area(self):
        """Method to find the area of Rectangle"""

        return self.__height * self.__width

    def display(self):
        """Method to print Rectangle out to stdout"""

        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.x + "#" * self.__width)

    def __str__(self):
        """Method to return string representation of Rectangle"""

        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """Method to assign arguments to attributes
        Args:
            args: List of arguments coming into the method
            kwargs: Dictionary with key:value of arguments given
        """

        if args:
            if len(args) == 1:
                self.id = args[0]
            if len(args) == 2:
                self.id = args[0]
                self.__width = args[1]
            if len(args) == 3:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
            if len(args) == 4:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
                self.__x = args[3]
            if len(args) == 5:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
                self.__x = args[3]
                self.__y = args[4]
        else:
            for key, value in kwargs.items():
                if key == "height":
                    self.__height = value
                if key == "id":
                    self.id = value
                if key == "width":
                    self.__width = value
                if key == "x":
                    self.__x = value
                if key == "y":
                    self.__y = value

    def to_dictionary(self):
        """Method to return dictionary representation of Rectangle"""

        dic = {
            "id": self.id,
            "width": self.__width,
            "height": self.__height,
            "x": self.__x,
            "y": self.__y
        }
        return dic
