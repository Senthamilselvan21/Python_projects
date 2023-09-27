import pymysql
connection = pymysql.connect(host="localhost",user="root",passwd="",database="employee")
cursor = connection.cursor()
print("Database connected successfully")
connection.close()
