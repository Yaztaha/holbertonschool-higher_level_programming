#!/usr/bin/python3
""" Read file """


def read_file(filename=""):
    """ Function that reads a file's content """
    with open(filename, encoding="UTF-8") as myFile:
        print(myFile.read(), end="")
