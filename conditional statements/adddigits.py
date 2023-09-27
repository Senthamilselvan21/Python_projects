n=int(input("Enter a number : "))
sum=0
rem=0
while n > 0:
    rem = n % 10
    n = n // 10
    sum = sum + rem
print("The sum is : ",sum)  
