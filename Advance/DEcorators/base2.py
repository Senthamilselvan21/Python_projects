class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        # self.gotmarks = self.name + ' obtained ' + self.marks + ' marks'

    def gotmarks(self):
        return self.name + ' obtained ' + self.marks + ' marks'


st = Student("Jaki", "25")
print(st.name)
print(st.marks)
print(st.gotmarks())

st.name = "Anusha"
print(st.name)
print(st.gotmarks())
