import sqlite3

#database connection
connection = sqlite3.connect("Employee.db")
cursor = connection.cursor()

# queries for inserting values
insert1 = "INSERT INTO Besant(ID,EMPID,NAME,DESIGNATION,EXPERIENCE,SALARY) VALUES(1,1004,'Abdul', 'SE',2,200000 );"
insert2 = "INSERT INTO Besant(ID,EMPID,NAME,DESIGNATION,EXPERIENCE,SALARY) VALUES(2,1001,'Kesavan', 'SSE',3,100000 );"
insert3 = "INSERT INTO Besant(ID,EMPID,NAME,DESIGNATION,EXPERIENCE,SALARY) VALUES(3,1002,'Vikash', 'SE',2,200000 );"
insert4 = "INSERT INTO Besant(ID,EMPID,NAME,DESIGNATION,EXPERIENCE,SALARY) VALUES(4,1003,'Disha', 'SE',2,200000 );"


#executing the quires
cursor.execute(insert1)
cursor.execute(insert2)
cursor.execute(insert3)
cursor.execute(insert4)


#commiting the connection then closing it.
connection.commit() 
connection.close()

