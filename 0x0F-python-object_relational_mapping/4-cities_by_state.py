#!/usr/bin/python3
""" Script that lists all cities from the database hbtn_0e_4_usa """
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    c = db.cursor()
    c.execute("SELECT cities.id, cities.name, states.name FROM cities \
INNER JOIN states on cities.state_id = states.id ORDER BY cities.id ASC")
    states_rows = c.fetchall()
    for row in states_rows:
        print(row)
    c.close()
    db.close()
