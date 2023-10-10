class student:
        def get_details(self):
                self.name="john"
                self.rno=429
                self.fee=50000.06
        def put_details(self):
                print("Name is:",self.name)
                print("Rno is",self.rno)
                print("Fee is:",self.fee)
obj=student()
obj.get_details()
obj.put_details()

