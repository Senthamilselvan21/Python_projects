import sqlite3

#database connection
connection = sqlite3.connect("Employee.db")
cursor = connection.cursor()
# Query for creating table
EmpTableSql = """CREATE TABLE Besant(
ID INT(20) ,
EMPID INT(20),
NAME  CHAR(20) NOT NULL,
DESIGNATION CHAR(10),
EXPERIENCE INT(20),
SALARY INT(20))"""
cursor.execute(EmpTableSql)
connection.close()

