class student(): #class defination
    def get_details(self): #Methods
        self.name="Jhon cena"
        self.rno=450
        self.fee=50000.26
    def put_details(self):
        print("Name is: ",self.name)
        print("Rno is : ",self.rno)
        print("Fees: ",self.fee)
obj=student() #object creation
obj.get_details()
obj.put_details()