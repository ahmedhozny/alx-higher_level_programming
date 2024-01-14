#!/usr/bin/python3

""" connects to a database and retrieves data from the 'states' table. """

import sys
import MySQLdb

if __name__ == "__main__":
	# Establish a connection to the MySQL database
	conn = MySQLdb.connect(
		host="localhost", user=sys.argv[1],
		passwd=sys.argv[2], db=sys.argv[3], port=3306)
	with conn.cursor() as cursor:
		cursor.execute("SELECT * FROM states")
	for row in cursor.fetchall():
		print(row)
	conn.close()
