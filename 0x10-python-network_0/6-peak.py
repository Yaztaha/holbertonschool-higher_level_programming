#!/usr/bin/python3
"""Function that finds a peak in a list of unsorted integers with the minimal time complexity"""


def find_peak(list_of_integers):
    """Method for finding the peak integer"""
    if len(list_of_integers) > 0:
        list_of_integers.sort()
        return list_of_integers[-1]
    else:
        return None
