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
    
    with db.cursor() as cur:
        cursor.execute("SELECT * FROM states \
                WHERE name LIKE BINARY %(name)s \
                ORDER BY states.id ASC")
                {
                    'name' = argv[4]
                }
                 
        rows = cursor.fetchall()

    if row is not None:
        for row in rows:
        print(row)