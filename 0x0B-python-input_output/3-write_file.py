#!/usr/bin/python3
""" Write a string to a text file """


def write_file(filename="", text=""):
    """ Function to write a string to a text file """

    with open(filename, mode="w", encoding="UTF-8") as myFile:
        return myFile.write(text)
