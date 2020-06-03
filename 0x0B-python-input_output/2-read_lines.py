#!/usr/bin/python3
""" Read n lines of a text file """


def read_lines(filename="", nb_lines=0):
    """ Function that reads n lines of a text file """
    with open(filename, encoding="UTF-8") as myFile:

        if nb_lines <= 0:
            print(myFile.read(), end="")
        else:
            counter = 0
            for line in myFile:
                if counter != nb_lines:
                    print(line, end="")
                    counter += 1
                else:
                    break
