def calc_factorial(x):
#    return (x * calc_factorial(x-1))
    if x == 1:
        return 1
    else:
        return (x * calc_factorial(x-1))
num = 5
fact=calc_factorial(num)
print("The factorial of", num, "is", fact)

'''
Forward calling         Backward Calling
5*calc_factorial(4)         5*24=120
4*calc_factorial(3)         4*6=24
3*calc_factorial(2)         3*2=6
2*calc_factorial(1)         2*1=2
1                                 1
'''
