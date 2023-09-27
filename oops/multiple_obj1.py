"""class employee:
    database="employee"
    def get_details(self,ename,eempid,esalary):
        self.name=ename
        self.empid=eempid
        self.salary=esalary
    def put_details(self):
        print("Employee name is: ",self.name)
        print("Employee ID: ",self.empid)
        print("Salary: ",self.salary)
        print("Database is: ",self.database)
container=[]
numofemp=int(input("Enter the number of employees: "))
for i in range(numofemp):
    name = input("Enter your name: ")
    empid = int(input("Enter your id: "))
    salary = float(input("Enter your salary: "))
    obj=employee()
    obj.get_details(name,empid,salary)
    container.append(obj)
print("*******************")
for i in range(numofemp):
    container[i].put_details()
    print("**********")
print("#################")
for obj in container:
    obj.put_details()
container[0].database=container[0].name
print("Class database: ",employee.database)
print("===============================")
for i in range(numofemp):
    container[i].put_details()
    print("*************************")
"""
class student:
    database="student"

    def __init__(self,aname,arollno,afees):
        self.name=aname
        self.rollno=arollno
        self.fees=afees

    def put_details(self):
        print("Name is : ",self.name)
        print("Roll no is : ",self.rollno)
        print("Fees is: ",self.fees)
        print("Database is: ",self.database)

container=[]
noofstud=int(input("Enter the number of details you needed: "))

for i in range(noofstud):
    name=input("Enter your name: ")
    roll_no=int(input("Enter your register number: "))
    fees=float(input("Enter your fees: "))

obj=student(name,roll_no,fees)
obj.put_details()
container.append(obj)

#for i in range(noofstud):
 #   container[i].put_details()
#for obj in container:
 #   obj.put_details()

for i in range(noofstud):
    container[0].database=container[0].name

for obj in container:
    obj.put_details()

