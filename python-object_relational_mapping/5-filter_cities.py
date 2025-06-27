#!/usr/bin/python3
"""Lists all cities of a given state from the database hbtn_0e_4_usa"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Récupérer les arguments : user, password, dbname, state_name
    user = sys.argv[1]
    passwd = sys.argv[2]
    dbname = sys.argv[3]
    state_name = sys.argv[4]

    # Connexion à la base de données
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=passwd,
        db=dbname
    )

    cur = db.cursor()

    # Requête SQL sécurisée avec placeholder (%s) pour éviter injection
    query = """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """
    cur.execute(query, (state_name,))

    # Récupérer tous les noms de villes
    cities = [row[0] for row in cur.fetchall()]

    # Afficher sous la forme demandée
    print(", ".join(cities))

    cur.close()
    db.close()
