class Person:
    name = ""
    age = 0
    def __init__(self, personName, personAge):
        self.name = personName
        self.age = personAge
    def display(self):
        print("Name is:",self.name)
        print("Age is:",self.age)
    def __del__(self):
        print("Base Destructor")

class Student(Person):
    studentId = ""
    fees=0.0
    def __init__(self, studentName, studentAge, studentId,fees):
        Person.__init__(self, studentName, studentAge)
        self.studentId = studentId
        self.fees = fees
    def getId(self):
        return self.studentId
    def getFee(self):
        return self.fees
    def __del__(self):
        print("Der Destructor")

print("Person Details are")
print("******************")
person = Person("Ricky Ponting", 50)
person.display()
print("******************")
print("Student Details are")
print("******************")
student = Student("Ganguly", 50, "129",50000)
student.display()
print("Student Id:",student.getId())
print("Student Fee:",student.getFee())
print("******************")

