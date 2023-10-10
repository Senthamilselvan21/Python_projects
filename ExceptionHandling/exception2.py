try:
    value1 = int(input("Enter a number1: "))
    value2 = int(input("Enter a number2: "))

    result = value1 / value2
    print("Result is: ", result)
except ValueError:
    print("ValueError:Exception Handler")
    print("Invalid input: Only integers are allowed")
except ZeroDivisionError:
    print("ZeroDivisionError:Exception Handler")
    print("OH!!!! divide a number by 0")
except IndentationError:
    print("IndentationError:Exception Handler")
print("After exception")
