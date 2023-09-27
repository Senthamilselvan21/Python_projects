class addOverload:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self,other):
         a = self.a + other.a
         b = self.b + other.b
         return addOverload(a,b)

    def display(self):
        print("a is : ", self.a)
        print("b is : ", self.b)


obj1 = addOverload(2,3)
obj2 = addOverload(2,2)
obj3 = addOverload(8,5)
obj = obj1+obj2+obj3
obj.display()
"""

o1=(2,3) o2=(2,2) o3=(8,5)

o=o1+o2+o3
o1+o2
self  + other
2+2     3+2
 
 4      5
 
 (4,5)
 
 (o1+o2) + o3
 4 + 8     5+5
 
 12         10
 
 (12,10)
"""
