#!/usr/bin/python3
""" Write an object to a text file """
import json


def save_to_json_file(my_obj, filename):
    """ Function that wrutes an obkedct to a text file """
    with open(filename, mode="w") as myFile:
        json.dump(my_obj, myFile)
