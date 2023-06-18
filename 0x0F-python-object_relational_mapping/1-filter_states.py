#!/usr/bin/python3
"""
Script that lists all states with a name starting with 'N' (uppercase N)
from the database hbtn_0e_0_usa
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    # Script arguments
    mysql_user = argv[1]
    mysql_password = argv[2]
    db_name = argv[3]

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

    # Select states with names starting with 'N'
    cursor.execute("""
        SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC
    """)

    # Fetch all rows
    states = cursor.fetchall()

    # Print the states
    for state in states:
        print(state)

    # Close cursor and database connections
    cursor.close()
    db.close()

