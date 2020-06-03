#!/usr/bin/python3
""" Append a string at the end of a file """


def append_write(filename="", text=""):
    """ Function that append a text at the end """

    with open(filename, mode="a", encoding="UTF-8") as myFile:
        return myFile.write(text)
