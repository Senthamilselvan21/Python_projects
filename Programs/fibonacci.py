
n = int(input("How many terms? "))

# first two terms
x = 0
y = 1
count = 0

if n <= 0:
   print("Please enter a positive integer")
elif n == 1:
   print("Fibonacci sequence upto",n,":")
   print(x)
else:
   print("Fibonacci sequence upto",n,":")
   while count < n:
       print(x,end=' , ')
       add = x + y
       # update values
       x = y
       y = add
       count += 1
   print("\n")
