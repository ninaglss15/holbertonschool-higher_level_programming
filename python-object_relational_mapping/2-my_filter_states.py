#!/usr/bin/python3
"""Script that lists states matching a given name from the database"""

import sys
import MySQLdb


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    cursor = db.cursor()

    # Use parameterized query to prevent SQL injection
    query = "SELECT * FROM states WHERE BINARY name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))
    rows = cursor.fetchall()

    # Print results
    for row in rows:
        print(row)

    # Clean up
    cursor.close()
    db.close()
