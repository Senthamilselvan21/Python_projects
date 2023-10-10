class student:
        def __init__(self,aname,arno,afee):
                self.name=aname
                self.rno=arno
                self.fee=afee
        def put_details(self):
                print("Name is:",self.name)
                print("Rno is",self.rno)
                print("Fee is:",self.fee)
        def __del__(self):
                print(self.name,":Object destroyed")
obj_s1=student("john",420,50000)
#obj_s1=student()
obj_s2=student("abraham",450,47000.0)
print("Object:1st Created Object Details")
obj_s1.put_details()
print("Object:2nd Created Object Details")
obj_s2.put_details()
del obj_s1
del obj_s2

