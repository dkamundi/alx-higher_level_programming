#!/usr/bin/python3
"""
Write a script that lists all cities from the database
"""

import MySQLdb
import sys

"""
code should not be executed when imported
"""

if __name__ == "__main__":
	# Open Connection
	connection = MySQLdb.connect(host='localhost',port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
	# close connection
	cursor = connection.cursor()
	sql = """SELECT cities.id, cities.name, states.name
	FROM cities
	JOIN states ON cities.state_id = states.id ORDER BY id ASC"""
	cursor.execute(sql)
	cities = cursor.fetchall()

	# Loop through
	for city in cities:
		print(city)
	
	# Close Cursor
	cursor.close()
	# close connection
	connection.close()
