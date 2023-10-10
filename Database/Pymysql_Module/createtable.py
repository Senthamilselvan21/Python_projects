import pymysql

#database connection
connection = pymysql.connect(host="localhost", user="root", passwd="", database="Employee")
cursor = connection.cursor()
# Query for creating table
EmpTableSql = """CREATE TABLE Besant(
ID INT(20) PRIMARY KEY AUTO_INCREMENT,
EMPID INT(20),
NAME  CHAR(20) NOT NULL,
DESIGNATION CHAR(10),
EXPERIENCE INT(20),
SALARY INT(20))"""
cursor.execute(EmpTableSql)
print("Table created Successfully")
connection.close()

