#!/usr/bin/python3
""" Lists states that begins with N """
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    c = db.cursor()
    c.execute("SELECT id, name FROM states WHERE name like 'N%' ORDER BY id")
    states_rows = c.fetchall()

    for i in range(len(states_rows)):
        print("{}".format(states_rows[i]))
