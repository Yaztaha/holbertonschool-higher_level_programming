#!/usr/bin/python3
""" JSON representation of a string """
import json


def to_json_string(my_obj):
    """ Function that return JSON representation of a string """
    return json.dumps(my_obj)
