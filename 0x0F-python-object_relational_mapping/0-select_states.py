#!/usr/bin/env python3
import sys
import MySQLdb

# Get command-line arguments
username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]

# Connect to the MySQL server
db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

# Create a cursor object to interact with the database
cursor = db.cursor()

# Execute the SQL query to retrieve all states
cursor.execute("SELECT * FROM states ORDER BY id ASC")

# Fetch all the rows from the result set
rows = cursor.fetchall()

# Print the states
for row in rows:
    print(row)

# Close the cursor and database connection
cursor.close()
db.close()

