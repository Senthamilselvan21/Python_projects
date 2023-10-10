import sqlite3

#database connection
connection = sqlite3.connect("Employee.db")
cursor = connection.cursor()


deleteSql = "DELETE FROM Besant WHERE ID = '1'; "
cursor.execute(deleteSql )


#commiting the connection then closing it.
connection.commit()
connection.close()
