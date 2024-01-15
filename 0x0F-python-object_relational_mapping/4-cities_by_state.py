#!/usr/bin/python3

""" connects to a database and retrieves from 'states' & 'cities' tables. """

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    query = ("SELECT cities.id, cities.name, states.name "
             "FROM cities, states "
             "WHERE states.id = cities.state_id")
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
