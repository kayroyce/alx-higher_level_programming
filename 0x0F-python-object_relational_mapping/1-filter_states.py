#!/usr/bin/python3
"""
python script that lists all states from the database hbtn_0e_0_usa with a name
starting with N
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY \
                   'N%' ORDER BY states.id;")
                 
    rows = cursor.fetchall()

    #for row in rows:
    #    print(row)

    # Another way to do it
    [print(state) for state in cur.fetchall() if state[1][0] == "N"]