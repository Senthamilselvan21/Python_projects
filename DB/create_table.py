"""import pymysql
database connection
#connection = pymysql.connect(host="localhost",user="root",passwd="",database="employee")
cursor = connection.cursor()
#query for creating table"""
EmpTableSql="""CREATE TABLE Besant(
ID INT(20) PRIMARY KEY AUTO_INCREMENT,
EMPID INT(20),
NAME CHAR(20) NOT NULL,
DESIGNATION CHAR(10),
EXPERIENCE INT(20),
SALARY INT(20))"""


"""cursor.execute(EmpTableSql)
print("Table create successfully")
connection.close()"""

import pymysql
#database connection
connection = pymysql.connect(host="localhost",user="root",passwd="",database="student")
cursor = connection.cursor()
StudTableSql="""CREATE TABLE Student(
NAME CHAR(20),
REGISTER_NO INT(20),
YEAR_OF_PASSING INT(20),
COURSE CHAR(20))"""
cursor.execute(StudTableSql)
print("Table create successfully")
connection.close()

