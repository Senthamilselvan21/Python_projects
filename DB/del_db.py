import pymysql

connection = pymysql.connect(host='localhost',user='root',passwd='',database='employee')
cursor = connection.cursor()

deletesql="DELETE FROM Besant WHERE ID ='2';"
cursor.execute(deletesql)


connection.commit()
print("deleted record successfully ")
connection.close()