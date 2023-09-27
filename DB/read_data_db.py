import pymysql

connection = pymysql.connect(host='localhost',user='root',passwd='',database='employee')
cursor = connection.cursor()

retrive = "Select * from Besant"


cursor.execute(retrive)
records= cursor.fetchall()
print("**************")
for record in records:
    print(record)
print("**************")
print("data readed successfully")