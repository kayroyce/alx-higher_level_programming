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
    cursor.execute("SELECT * FROM states")
    rows = cursor.fetchall()
<<<<<<< HEAD

    for row in rows:
        print(row)
=======
    
    for row in rows:
            print(row)
    
>>>>>>> 0b9fe86ea6ac23bdb5d744a62231b1ca22b12280
