global_var=50
def sample():
    local_var=30
    global_var=100
    print("Inside function global variable is: ",global_var)
    print("Inside function  local variable is : ",local_var)
sample()
print("The global variable outside function: ",global_var)
#print("The  local  variable outside function: ",local_var)
# Because we can't access the local variable outside the function
print("-------------------------------------------------------------")
global_var=50
def sample():
    global global_var # here we define again global_var as global so that we get this data as global
    local_var=30
    global_var=100
    print("Inside function global variable is: ",global_var)
    print("Inside function  local variable is : ",local_var)
sample()
print("The global variable outside function: ",global_var)