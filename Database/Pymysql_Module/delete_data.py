import pymysql

#database connection
connection = pymysql.connect(host="localhost", user="root", passwd="", database="Employee")
cursor = connection.cursor()


deleteSql = "DELETE FROM Besant WHERE ID = '1'; "
cursor.execute(deleteSql )


#commiting the connection then closing it.
connection.commit()
print("Deleted Record successfully")
connection.close()
