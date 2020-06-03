#!/usr/bin/python3
""" Create an object from JSON file """
import json


def load_from_json_file(filename):
    """ Function that creates an object from a JSON file """
    with open(filename, mode="r") as myFile:
        return json.load(myFile)
