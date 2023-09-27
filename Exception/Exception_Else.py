
try:
    num1 = int(input("Enter a number1: "))
    num2 = int(input("Enter a number2: "))
    result=num1/num2
    print("Result is: ",result)
except ZeroDivisionError as e:
    print("Zero division error occured:",e)
    print("After logic")
else:
    print("try block successfully executed") # To check whether the try block is fully executed or not.