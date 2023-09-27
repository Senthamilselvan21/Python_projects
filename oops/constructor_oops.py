class student:
    def __init__(self,aname,arno,afee): # Constructor it will automatically  call once the class created or initiated with the object
        self.name=aname
        self.rno=arno
        self.fee=afee
    def put_details(self):
        print("Name is : ",self.name)
        print("Roll no: ",self.rno)
        print("Fees is: ",self.fee)

    def __del__(self): # Destructor it will automatically call when we initiate del in the program
        print(self.name,": Object destroyed")
obj_1=student("Jhon_cena",34,4000) #obj1 created with the class student
obj_2=student("Shimus",22,70000) # """""""""""""""""""""""""""""""""""
print("Object 1 is created ")
obj_1.put_details()  # obj1 details will be substituted to put details
print("Object 2 is created")
obj_2.put_details()

del obj_1 # used to delete a object
del obj_2