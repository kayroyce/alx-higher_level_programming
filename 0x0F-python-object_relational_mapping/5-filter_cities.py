#!/usr/bin/python3
"""
Script that lists all `cities` in the `cities` table of `hbtn_0e_4_usa`
where the city's state matches the argument `state name`.
Arguments:
    mysql username (str)
    mysql password (str)
    database name (str)
    state name (str)
"""

import sys
import MySQLdb

if __name__ == "__main__":
    mySQL_u = sys.argv[1]
    mySQL_p = sys.argv[2]
    db_name = sys.argv[3]

    state_name = sys.argv[4]

    # By default, it will connect to localhost:3306
    db = MySQLdb.connect(user=mySQL_u, passwd=mySQL_p, db=db_name)
    cur = db.cursor()

    cur.execute("SELECT cities.name, state.name FROM cities\
                 INNER JOIN states ON cities.state_id = states.id \
                 ORDER BY cities.id")
    rows = cur.fetchall()

    new = [pair[1] for pair in cur.fetchall() if argv[4] == pair[0]]
    print("'" join(new))
    
    #for i in range(len(rows)):
    #    print(rows[i][0], end=", " if i + 1 < len(rows) else "")
    #print("") if argv[4 ]