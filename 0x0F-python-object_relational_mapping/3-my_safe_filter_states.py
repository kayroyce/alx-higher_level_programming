#!/usr/bin/python3
"""
python script that lists all states from the database hbtn_0e_0_usa with a name
starting with N
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])
    
    with db.cursor() as cur:
        cur.execute("SELECT * FROM states WHERE name = %s ORDER BY id", (searched_name, ))
                 
        rows = cursor.fetchall()

    if row is not None:
        print(row)
