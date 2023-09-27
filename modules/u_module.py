"""import calculator
a = int(input("Enter a value: "))
b = int(input("Enter a value: "))
print("Addition is : ",calculator.sume(a,b))
print("Subtraction is : ",calculator.subs(a,b))
print("Multiplication is : ",calculator.mul(a,b))
print("Division is : ",calculator.div(a,b))
print("Modulus is : ",calculator.mod(a,b))
print("String is : ",calculator.string)"""



from calculator import sume,subs,mul,div,mod,string
a = int(input("Enter a value: "))
b = int(input("Enter a value: "))
print("Addition is : ",sume(a,b))
print("Subtraction is : ",subs(a,b))
print("Multiplication is : ",mul(a,b))
print("Division is : ",div(a,b))
print("Modulus is : ",mod(a,b))
print("String is : ",string)