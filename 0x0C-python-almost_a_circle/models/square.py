#!/usr/bin/python3
"""Module containing Square class"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Init method
        Args:
            size: Size of the Square
            x: X position
            y: Y position
            id: ID of the object created
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter method for size"""

        return self.width

    @size.setter
    def size(self, value):
        """Validator setter method for size"""

        self.width = value
        self.height = value

    def __str__(self):
        """Method to return string representation of Square"""

        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.height)

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
                self.__size = args[1]
            if len(args) == 3:
                self.id = args[0]
                self.__size = args[1]
                self.x = args[2]
            if len(args) == 4:
                self.id = args[0]
                self.__size = args[1]
                self.x = args[2]
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == "size":
                    self.__size = value
                if key == "id":
                    self.id = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """Method to return dictionary representation of Square"""

        dic = {
            "id": self.id,
            "size": self.__size,
            "x": self.x,
            "y": self.y
        }
        return dic
