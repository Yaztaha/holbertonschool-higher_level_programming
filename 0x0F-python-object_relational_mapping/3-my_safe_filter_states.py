#!/usr/bin/python3
""" Script that handles SQL injection """
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    c = db.cursor()
    c.execute("SELECT * FROM states WHERE \
    states.name =%s ORDER BY id ASC", (argv[4],))
    states_rows = c.fetchall()
    for state in states_rows:
        print(state)
    c.close()
    db.close()
