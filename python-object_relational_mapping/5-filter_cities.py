#!/usr/bin/python3
"""Lists all cities of a given state from the database hbtn_0e_4_usa."""

import MySQLdb
import sys


if __name__ == "__main__":
    user = sys.argv[1]
    pwd = sys.argv[2]
    dbname = sys.argv[3]
    state = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=pwd,
        db=dbname
    )

    cur = db.cursor()
    query = (
        "SELECT cities.name FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "WHERE states.name = %s "
        "ORDER BY cities.id ASC"
    )
    cur.execute(query, (state,))
    rows = cur.fetchall()
    names = [r[0] for r in rows]
    if names:
        print(", ".join(names))

    cur.close()
    db.close()
