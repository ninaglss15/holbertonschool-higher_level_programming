#!/usr/bin/python3
"""List all states starting with 'N' from the database using MySQLdb"""

import sys
import MySQLdb


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to the MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    cursor = db.cursor()

    # Execute SQL query selecting states starting with 'N'
    cursor.execute(
        "SELECT * FROM states WHERE BINARY name LIKE 'N%' ORDER BY id ASC"
    )
    results = cursor.fetchall()

    # Print each row from the result
    for row in results:
        print(row)

    # Close cursor and connection
    cursor.close()
    db.close()
