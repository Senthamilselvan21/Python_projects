"""
syntax:
        lambda args:expression
"""
double = lambda x:x*2
#def double(x):
 #   return x*2
x = int(input("Enter a value: "))
value = double(x)
print("value is : ",value)