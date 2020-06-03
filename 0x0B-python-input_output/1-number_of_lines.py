#!/usr/bin/python3
""" Retrun number of lines of a text file """


def number_of_lines(filename=""):
    """ Function that reads the number of lines of a text file """

    with open(filename, encoding="UTF-8") as myFile :

        for counter, line_n in enumerate(myFile):
            pass
    return counter+1
