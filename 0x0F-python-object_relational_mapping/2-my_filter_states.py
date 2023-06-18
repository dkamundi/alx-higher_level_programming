#!/usr/bin/python3
"""
Script that displays all values in the states table of hbtn_0e_0_usa where
name matches the argument
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    # Script arguments
    mysql_user = argv[1]
    mysql_password = argv[2]
    db_name = argv[3]
    state_name = argv[4]

    # Connect to MySQL database
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=mysql_user,
        passwd=mysql_password,
        db=db_name
    )

    # Create cursor to execute queries
    cursor = db.cursor()

    # Select states matching the provided name
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))

    # Fetch all rows
    states = cursor.fetchall()

    # Print the states
    for state in states:
        print(state)

    # Close cursor and database connections
    cursor.close()
    db.close()

