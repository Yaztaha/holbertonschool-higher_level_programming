#!/usr/bin/python3
""" Rectangle module """


class Rectangle:
   """ rectangle class """

   def __init__(self, width=0, height=0):
       """ Initialization method with height and width """
       self.width = width
       self.height = height

   @property
   def width(self, value):
      """ Rectangle width getter """
      return self.__width

   @width.setter
   def width(self, value):
      """ Rectangle width setter """
      if type(value) is not int:
         raise TypeError("width must be an integer")
      elif value < 0:
         raise TypeError("width must be >=0")
      else:
         self.__width = value

   @property
   def height(self, value):
      """ Rectangle height getter """
      return self.__height

   @height.setter
   def height(self, value):
      """ Rectangle height setter """
      if type(value) is not int:
         raise TypeError("height must be an integer")
      elif value < 0:
         raise TypeError("height must be >= 0")
      else:
         self.__height = value

   def area(self):
      """ Rectangle area """
      return self.__height * self.__width

   def perimeter(self):
      """ Rectangle perimeter """
      return (self.__height + self.__width) * 2
