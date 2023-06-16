#!/usr/bin/env python3
import sys
import MySQLdb

#Get coommand-line arguements
username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]

#Connect to MySQL server
db = MySQLdb.connect(host="localhost",port=3306, user=username, passwd=password, db=database)

#create a cursor object to interract with the database
cursor = db.cursor()

#Execue the SQL query to retrieve all states
cursor.execute("SELECT * FROM states ORDER BY id ASC")

#Fetch all rows from the result set
row = cursor.fetchall()

#Print the states
for row in rows:
    print(row[1])

#Close the cursor and database connection
cursor.close()
db.close()

