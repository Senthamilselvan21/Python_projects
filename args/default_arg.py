# rules and regulations of default arguments
"""
def default_arg_fun(a=10,b=10,c=10):right
def default_arg_fun(a,b=10,c=30):right
def default_arg_fun(a=10,b,c=10):wrong
def default_arg_fun(a=10,b,c):wrong
def default_arg_fun(a=10,b=20,c):wrong
def default_arg_fun(a,b=20,c):wrong
"""

#def default_arg_fun(a,b=10,c=30)
def default_arg_fun(a=10,b=20,c=30):
    print("The value of a is : ",a)
    print("The value of b is :  ",b)
    print("The value of c is : ",c)

x=1
y=2
z=3
print("Calling without Args")
default_arg_fun()
print("Calling with single argument")
default_arg_fun(x)
print("Calling with two arguments")
default_arg_fun(x,y)
print("Calling with two arguments")
default_arg_fun(x,z)
print("Calling with three arguments")
default_arg_fun(x,y,z)