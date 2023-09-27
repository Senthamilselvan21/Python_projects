import pymysql
connection = pymysql.connect(host="localhost",user='root',passwd='',database='student')
cursor = connection.cursor()


def table_create():
    id = int(input("Enter your id: "))
    name = input("Enter name: ")
    year_of_passing = int(input("Enter yop: "))
    mobile = int(input("Enter phno: "))
    course = input("Enter your course: ")
    table_name=input("Enter table name: ")
    table = """CREATE TABLE {}(ID INT(20),NAME CHAR(20),YOP INT(20),MOBILE INT(20),COURSE CHAR(20))
    """.format(table_name)
    cursor.execute(table)
    insert_data = "INSERT INTO {}(ID,NAME,YOP,MOBILE,COURSE) VALUES({},{},{},{},{});".format(table_name,id,name,year_of_passing,mobile,course)
    cursor.execute(insert_data)
connection.commit()

def show_data():
    table_name = input("Enter table name: ")
    get = "SELECT * FROM {} ".format(table_name)
    cursor.execute(get)
    record = cursor.fetchall()
    for records in record:
        print(records)
def update_db():
    table_name = input("Enter table name: ")
    id=int(input("Enter your id: "))
    name1 = input("Enter name: ")
    yop = int(input("Enter yop: "))
    no = int(input("Enter phno: "))
    courses = input("Enter your course: ")
    update = "UPDATE {} SET NAME={},YOP={},MOBILE={},COURSE={} WHERE ID={};".format(table_name,name1,yop,no,courses,id)
    cursor.execute(update)
connection.commit()

def delete_data():
    id = int(input("Enter your id: "))
    del_data="DELETE FROM STUD WHERE ID={};".format(id)

    cursor.execute(del_data)
connection.commit()

def drop_table():
    table_name = input("Enter table name: ")
    dt = "DROP TABLE IF EXISTS {};".format(table_name)
    cursor.execute(dt)
    print("Table deleted successfully")
connection.commit()



print("List of operations\n 1.create table\n2.show data\n3.update\n4.delete\n5.drop\n6.exit")
i = int(input("Select your choice: "))
while i < 6:
    if i == 1:
        table_create()
    elif i == 2:
        show_data()
    elif i ==3:
        update_db()
    elif i == 4:
        delete_data()
    elif i == 5:
        drop_table()
        break
    else:
        print("Provide correct input")








