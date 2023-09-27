name=input("Enter your name: ")
reg_no = int(input("Enter your register number: "))
year_of_passing=int(input("Enter your YOP: "))
course=input("Enter your course: ")
import pymysql
connection = pymysql.connect(host="localhost",user="root",passwd="",database="student")
cursor = connection.cursor()

record1="INSERT INTO Student(NAME,REGISTER_NO,YEAR_OF_PASSING,COURSE) VALUES(%s,%s,%s,%s);"
cursor.execute(record1,(name,reg_no,year_of_passing,course))
connection.commit()
print("Value inserted successfully")
connection.close()