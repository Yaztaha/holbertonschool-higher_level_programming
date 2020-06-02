#!/usr/bin/python3
""" Same class module """


def is_kind_of_class(obj, a_class):
    """ Function that checks if an object is an instance """

    if isinstance(obj, a_class):
        return True
    else:
        return False
