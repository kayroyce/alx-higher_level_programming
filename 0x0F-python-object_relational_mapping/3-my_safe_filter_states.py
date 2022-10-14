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
<<<<<<< HEAD
        cursor.execute(("SELECT * FROM states \
                WHERE name LIKE BINARY %(name)s \
                ORDER BY states.id ASC")
                {
                    'name' = argv[4]
                });
=======
        cur.execute("SELECT * FROM states WHERE name = %s ORDER BY id", (searched_name, ))
>>>>>>> 3db0ac7e614545e2ff400d2b4973fa913161cb7d
                 
        rows = cursor.fetchall()

    if row is not None:
<<<<<<< HEAD
        for row in rows:
        print(row)
=======
        print(row)

>>>>>>> 3db0ac7e614545e2ff400d2b4973fa913161cb7d
