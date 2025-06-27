#!/usr/bin/python3
"""Safely displays all values in the states table where name matches the argument"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get credentials and search value from args
    user = sys.argv[1]
    passwd = sys.argv[2]
    dbname = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=passwd,
        db=dbname
    )

    # Create cursor
    cur = db.cursor()

    # Use parameterized query to prevent SQL injection
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cur.execute(query, (state_name,))

    # Fetch and print results
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Cleanup
    cur.close()
    db.close()
