#!/usr/bin/python3
""" Base geometry module & rectangle subclass """
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle class """
    def __init__(self, width, height):
        """ method for width and height """
        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height

    def area(self):
        """ Method to determine rectangle's area """
        return self.__width * self.__height

    def __str__(self):
        """ Display rectangle's area """
        return("[Rectangle] {}/{}".format(self.__width, self.__height))
