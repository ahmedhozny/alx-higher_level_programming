#!/usr/bin/python3

""" connects to a database and retrieves from 'states' & 'cities' tables. """

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    query = (
        "SELECT cities.name "
        "FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "WHERE states.name = %s "
        "ORDER BY cities.id"
    )

    cur.execute(query, (sys.argv[4],))
    rows = cur.fetchall()
    res = []
    for row in rows:
        res.append(row[0])
    print(*res, sep=", ")
    cur.close()
    db.close()
