try:
    num1 = int(input("Enter a number1: "))
    num2 = int(input("Enter a number2: "))
    result=num1/num2
    print("Result is: ",result)
except ZeroDivisionError as e:
    print("Zero division error occured:",e)

else:
    print("try block successfully executed")
finally:
    print("I am always execute either success or failure")
print("After logic")