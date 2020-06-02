#!/usr/bin/python3
""" Module to check if object is an instace of a inherited class
"""


def inherits_from(obj, a_class):
    """ Function that checks if the object is an instance of a class that
    inherited (directly or indirectly) from the specified class """

    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    else:
        return False
