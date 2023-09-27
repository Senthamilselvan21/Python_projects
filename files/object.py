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

    def __str__(self):
        print(f"Name: {self.name},Roll no: {self.rollno},fees: {self.fees},Database: {self.database}")

container=[]
noofstud=int(input("Enter the number of details you needed: "))

for i in range(noofstud):
    name=input("Enter your name: ")
    roll_no=int(input("Enter your register number: "))
    fees=float(input("Enter your fees: "))

obj=student(name,roll_no,fees)
obj.put_details()
container.append(obj)

for i in obj.put_details():
    with open("sample.txt","a") as f:
        print(f.write(i))


#for i in range(noofstud):
 #   container[0].database=container[0].name

#for obj in container:
 #   obj.put_details()
