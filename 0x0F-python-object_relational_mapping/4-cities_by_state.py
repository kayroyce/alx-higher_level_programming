#!/usr/bin/python3
"""
Script that lists all `cities` from the database `hbtn_0e_4_usa`.
"""

import sys
import MySQLdb

if __name__ == "__main__":

    # By default, it will connect to localhost:3306
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    cur = db.cursor()

    cur.execute("SELECT cities.id, cities.name, states.name \
                FROM cities INNER JOIN states  ON cities.states_id = states.id \ 
                ORDER BY cities.id ASC")
    rows = cur.fetchall()

    for row in rows:
        print(row)