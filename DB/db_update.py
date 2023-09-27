import pymysql

connection = pymysql.connect(host='localhost',user='root',passwd='',database='employee')
cursor = connection.cursor()

updatesql="UPDATE Besant SET EMPID=1007,NAME='VIJAY',DESIGNATION='CE',EXPERIENCE=3,SALARY=30000 WHERE ID=4 ;"
cursor.execute(updatesql)
print("Data UPDATED successfully")
connection.close()