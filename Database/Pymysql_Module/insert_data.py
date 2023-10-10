import pymysql

#database connection
connection = pymysql.connect(host="localhost", user="root", passwd="", database="Employee")
cursor = connection.cursor()

# queries for inserting values
insert1 = "INSERT INTO Besant(EMPID,NAME,DESIGNATION,EXPERIENCE,SALARY) VALUES(1001,'Abdul', 'SE',2,200000);"
insert2 = "INSERT INTO Besant(EMPID,NAME,DESIGNATION,EXPERIENCE,SALARY) VALUES(1002,'Kesavan', 'SSE',3,100000);"
insert3 = "INSERT INTO Besant(EMPID,NAME,DESIGNATION,EXPERIENCE,SALARY) VALUES(1003,'Vikash', 'SE',2,200000);"
insert4 = "INSERT INTO Besant(EMPID,NAME,DESIGNATION,EXPERIENCE,SALARY) VALUES(1004,'Disha', 'SE',2,200000);"


#executing the quires
cursor.execute(insert1)
cursor.execute(insert2)
cursor.execute(insert3)
cursor.execute(insert4)


#commiting the connection then closing it.
connection.commit()
print("Data Inserted Successfully") 
connection.close()

