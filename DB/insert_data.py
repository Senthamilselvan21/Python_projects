import pymysql
#database connection
connection = pymysql.connect(host="localhost",user="root",passwd="",database="employee")
cursor = connection.cursor()

#queries for inserting values
name = "Senthamil"
record1 = "INSERT INTO Besant(EMPID,NAME,DESIGNATION,EXPERIENCE,SALARY) VALUES(1001,'%s','SE','2',200000);"%(name)
record2 = "INSERT INTO Besant(EMPID,NAME,DESIGNATION,EXPERIENCE,SALARY) VALUES(1002,'RAMAN','SSE',3,30000);"
record3 = "INSERT INTO Besant(EMPID,NAME,DESIGNATION,EXPERIENCE,SALARY) VALUES(1003,'MUNIRAJ','SE',2,40000);"
record4 = "INSERT INTO Besant(EMPID,NAME,DESIGNATION,EXPERIENCE,SALARY) VALUES(1004,'RAHUL','SE',2,200000);"

#executing the queries
cursor.execute(record1)
cursor.execute(record2)
cursor.execute(record3)
cursor.execute(record4)
#commenting the connection then closing it.
connection.commit()
print("Data inserted successfully")
connection.close()