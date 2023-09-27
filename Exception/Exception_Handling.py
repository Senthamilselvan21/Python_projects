"""
Syntax:
    try:
        logic
    except:
        exception
"""
# Zero division error
"""num1=int(input("Enter a number1: "))
num2=int(input("Enter a number2: "))
try:
    result=num1/num2
    print("Result is: ",result)
except ZeroDivisionError:
    print("Zero division error occured")
print("After logic")"""

# Value error
"""try:
    num1 = int(input("Enter a number1: "))
    num2 = int(input("Enter a number2: "))
    if num1 % num2 ==0 :
        print("It is even  ")
    else:
        print("IT is odd")
except ValueError:
    print("Value error occured input must be integer ")"""

#Module error

"""try:
    import calculator
    import cv2
    print("Module imported successfully")
except ModuleNotFoundError as e: # e is used to print the actual error as a statement
    print("Module not found:",e)"""
# Exception as e
num1=int(input("Enter a number1: "))
num2=int(input("Enter a number2: "))
try:
    result=num1/num2
    print("Result is: ",result)
except ZeroDivisionError as e:
    print("Zero division error occured:",e)
print("After logic")

