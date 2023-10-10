import sqlite3

#database connection
connection = sqlite3.connect("Employee.db")
cursor = connection.cursor()
# some other statements  with the help of cursor
connection.close()

