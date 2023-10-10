#rules and regulations of default arguments
'''
def default_arg_fun(a=10,b=20,c=30):Right
def default_arg_fun(a,b=20,c=30): right
def default_arg_fun(a,b,c=30): right
def default_arg_fun(a=10,b,c=30): wrong
def default_arg_fun(a=10,b=20,c): wrong
def default_arg_fun(a,b=20,c): wrong
'''
#def default_arg_fun(a=10,b,c=30): 
def default_arg_fun(a=10,b=20,c=30): 
        print("Value a is:",a) 
        print("Value b is:",b) 
        print("Value c is:",c) 
x=1 
y=2 
z=3 
print("Calling without Args") 
default_arg_fun() 
print("Calling with single Arg") 
default_arg_fun(x) 
print("Calling with two Args") 
default_arg_fun(x,y) 
print("Calling with two Args") 
default_arg_fun(x,z) 
print("Calling with three Args") 
default_arg_fun(x,y,z)

