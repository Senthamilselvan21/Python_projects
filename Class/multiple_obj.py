class student:
        database="student"
        def get_details(self,aname,arno,afee):
                self.name=aname
                self.rno=arno
                self.fee=afee
        def put_details(self):
                print("Name is:",self.name)
                print("Rno is",self.rno)
                print("Fee is:",self.fee)
                print("Database is:",self.database)
obj_container=[]
numOfObjs=int(input("Enter to create Number of Objects:"))
for i in range(numOfObjs):
    name   = str(input("Enter a Name:"))
    rollNo = int(input("Enter Roll Number:"))
    fees   = float(input("Enter fees:"))
    obj    = student()
    obj.get_details(name,rollNo,fees)
    obj_container.append(obj)
print("**************")
for i in range(numOfObjs):
    obj_container[i].put_details()
    print("*************")
obj_container[0].database=obj_container[0].name
print("Class database:",student.database)
for i in range(numOfObjs):
    obj_container[i].put_details()
    print("*************")

