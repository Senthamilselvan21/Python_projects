from collections import namedtuple
Student = namedtuple('Student', 'fname, sname, age')  
s = Student('Ritika', 'koti', '18')  
print(s.fname)
print(s.sname)
print(s.age)
