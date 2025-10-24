#!/usr/bin/python3
"""
This module makes a query to the database hbtn_0e_0_usa
"""
import sys
import MySQLdb


if __name__ == "__main__":
    try:
        # Check if all arguments are provided
        if len(sys.argv) != 4:
            print("Usage: {} username password database".format(sys.argv[0]))
            sys.exit(1)

        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
        )

        cursor = db.cursor()
        cursor.execute("SELECT * FROM states ORDER BY id ASC")
        rows = cursor.fetchall()
        for row in rows:
            print(row)

        cursor.close()
        db.close()
    except MySQLdb.Error as e:
        print("MySQL Error: {}".format(e))
        sys.exit(1)