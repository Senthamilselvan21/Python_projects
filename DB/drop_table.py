import pymysql

#database connection
connection = pymysql.connect(host='localhost',user='root',passwd='',database='student')
cursor = connection.cursor()

dropsql="DROP TABLE IF EXISTS stud_info;"
cursor.execute(dropsql)

#commiting the connection and the closing it
connection.commit()
print("Table has been deleted successfully")
connection.close()