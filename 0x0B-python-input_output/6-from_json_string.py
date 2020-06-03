#!/usr/bin/python3
""" Python data structure represented by JSON """
import json


def from_json_string(my_str):
    """ Function that return an object represented by JSON """
    return json.loads(my_str)
