def factorial(n):
    if  not isinstance(n, int):
        print("Invalid Argument type")
        raise RuntimeError("Argument must be int")

    if n < 0:
        print("Argument must be >= 0")
        raise RuntimeError("Argument must be >= 0")

    f = 1
    for i in range(n):
        f *= n
        n -= 1

    return f

try:
    value=int(input("enter number")) 
    #print("Factorial of ",value," is:", factorial(value))
    print("Factorial of ",value," is:", factorial(value))
except RuntimeError:
    print("Invalid Input")
