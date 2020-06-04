#!/usr/bin/python3
""" Script that adds all arguements to a Python list, ans then save them to a file """
import json
import sys
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

py_list = []

try:
    py_list = load_from_json_file("add_item_json")
    save_to_json_file(py_list + sys.argv[1:], "add_item.json")
except:
    save_to_json_file(py_list + sys.argv[1:], "add_item.json")
