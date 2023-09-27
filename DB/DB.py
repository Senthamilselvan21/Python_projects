import pymysql
connection = pymysql.connect(host='localhost',user='root',passwd='',database='student')
cursor = connection.cursor()
print("Connection Succeed")
Studtable=""" CREATE TABLE stud_info(
NAME CHAR(20),
COURSE CHAR(20),
MOBILE_NO INT(10),
YEAR_OF_PASSING INT(5),
FEES INT(10))
"""
cursor.execute(Studtable)
print("Table created successfully")

name=input("Enter your name: ")
course=input("Enter your course: ")
mobile_no = int(input("Enter your register number: "))
year_of_passing=int(input("Enter your YOP: "))
fees = int(input("Enter your fees"))
Inser_val="INSERT INTO stud_info(NAME,COURSE,MOBILE_NO,YEAR_OF_PASSING,FEES) VALUES(%s,%s,%s,%s,%s)"
cursor.execute(Inser_val,(name,course,mobile_no,year_of_passing,fees))
connection.commit()
print("Value inserted successfully")
connection.close()