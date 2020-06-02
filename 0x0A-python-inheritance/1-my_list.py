#!/usr/bin/python3
""" My list module """


class MyList(list):
    """  MyList sub_class that inherits from super_class list """

    def print_sorted(self):
        """ Print list """

        print(sorted(self))
