def calculation(a,b):#this is fuction defination 
        add=a+b 
        sub=a-b 
        mul=a*b 
        return add,sub,mul 
a=int(input("Enter a number:")) 
b=int(input("Enter a number:")) 
#x,y,z=calculation(a,b)#this is function call 
add,sub,mul=calculation(a,b)#this is function call 
print("Addition is :",add) 
print("Substraction is :",sub) 
print("Multiplication is :",mul) 

