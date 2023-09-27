"""def sum_of_digits(n):
    if n < 10:
        return n
    else:
        return n%10+sum_of_digits(n//10)
        
n=int(input("Enter a number: "))
sum_of_digits(n)
print("Sum of digits: ",sum_of_digits(n))"""

def sum_of_digits():
    n=int(input("Enter a number: "))
    sum=0
    for digits in str(n):
        sum=sum+int(digits)

sum_of_digits()
print("Sum of digits: ",sum)
        


