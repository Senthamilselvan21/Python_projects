import sqlite3

#database connection
connection = sqlite3.connect("Employee.db")
cursor = connection.cursor()


dropSql = "DROP TABLE IF EXISTS Besant;"
cursor.execute(dropSql)

#commiting the connection then closing it.
connection.commit()
connection.close()
