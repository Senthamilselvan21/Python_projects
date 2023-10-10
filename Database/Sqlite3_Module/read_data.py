import sqlite3

#database connection
connection = sqlite3.connect("Employee.db")
cursor = connection.cursor()

# queries for retrievint all rows
retrive = "Select * from Besant;"

#executing the quires
cursor.execute(retrive)
records = cursor.fetchall()
for record in records:
	print(record)

