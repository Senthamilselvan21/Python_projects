import sqlite3

#database connection
connection = sqlite3.connect("Employee.db")
cursor = connection.cursor()

updateSql = "UPDATE  Besant  SET NAME= 'Besant'  WHERE ID = '1' ;"
cursor.execute(updateSql)


#commiting the connection then closing it.
connection.commit()
connection.close()

