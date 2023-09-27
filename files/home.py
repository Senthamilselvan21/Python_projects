class Student:
    database = "student"

    def __init__(self, name, no, a_class, avg):
        self.name = name
        self.no = no
        self.a_class = a_class
        self.avg = avg

    def put_details(self, file):
        file.write("{}\t".format(self.name))
        file.write("{}\t".format(self.no))
        file.write("{}\t".format(self.a_class))
        file.write("{}\t".format(self.avg))
        file.write("\n")
    def once(self,file):
        file.write("Name  No  Class  Avg\n")

container = []
no_of_reports = int(input("Enter number of reports: "))
for i in range(no_of_reports):
    name = input("Enter your name: ")
    no = int(input("Enter your number: "))
    a_class = input("Enter your class: ")
    average = float(input("Enter your average: "))
    obj = Student(name, no, a_class, average)
    container.append(obj)

with open("sample.txt","r") as file:
    read = file.read()
    sp = read.split()
    for i in sp:
        if i == name:
            print("Value is already in the database ")
            continue
        else:
            output_file_name = "sample.txt"
            with open(output_file_name, "w") as output_file:
                for student_details in container:
                    student_details.once(output_file)
                    break
                for student_details in container:
                    student_details.put_details(output_file)

print("Details stored in the file:", output_file_name)
