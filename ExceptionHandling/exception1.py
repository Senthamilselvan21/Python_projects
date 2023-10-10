a=int(input("Enter a Number1:"))
b=int(input("Enter a Number2:"))
#res=a/b
#print ("Result is:",res)
try:
    res=a/b
    print ("Result is:",res)
except ZeroDivisionError:
    print ("ZeroDivisionError is raising an exception")

print("After result")

