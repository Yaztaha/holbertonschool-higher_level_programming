#!/usr/bin/python3
""" Script that takes in an argument and displays all values in
the states table
of hbtn_0e_0_usa where name matches the argument """
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    c = db.cursor()
    q = "SELECT id, name FROM states\
    WHERE name = (%s) ORDER BY states.id".format(argv[4])
    c.execute(q, [argv[4]])
    states_rows = c.fetchall()

    for i in range(len(states_rows)):
        print("{}".format(states_rows[i]))
