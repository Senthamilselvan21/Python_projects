# if we need to justify two conitions use if and else statements
"""age=int(input("Enter your age : "))
if age >=18:
    print("You are Eligible for voting")
else:
    print("You are not eligible for voting")"""

# if we need only a single condition use only if statement

"""age=int(input("Enter your age : "))
if age >=18:
    print("You are Eligible for voting")
print("You are not eligible for voting")"""

# More than two means use if,elif,else
# else only used for debugging purposes only in elif statements

"""
syntax
if condition 1:
    staements
elif condition:
    statements
elif condition:
    statements
elif condition:
    statements
else:
    statements"""


"""a=int(input("Enter a number : "))
b=int(input("Enter a number : "))
c=int(input("Enter a number : "))

if a>b and a>c:
    print("a is greater than others")
elif b>a and b>c:
    print("b is greater than others")
elif c>a and c>b:
    print("c is greater than others")
else:
    print("Use only different numbers!!!")"""


#<------------------------------------------------------>
#for loop

#syntax for variable name in range(start,stop,stepszie)

"""for i in range(7):
    print("value is: ",i)
print("**************************")
for i in range(1,10):
    print("value is: ",i)
print("**************************")
for i in range(1,10,2):
    print("The values is :",i)
print("**************************")"""

#<------------------------------------------------------------>
#While loop

#syntax
"""while condition:
    statements
    updation/modification
"""

"""i=0
while i <= 10:
    print("The values are : ",i)
    i+=1
print("Existing from loop")"""


"""for i in range(1,3):
    print("Row ",i, end=" ")
    for j in range(1,5):
         print(j)"""

# program to execute columns and rows
"""rcStart=1
nRows=4
nCol=5
for row in range(rcStart,nRows):   #1<4
    print("Row",row)    #printing row
    for col in range(rcStart,nCol):
        print("column: ",col)"""

#While loop

row=1
col=1
nrows=4
ncol=5
while row<nrows :
    print("Rows: ",row)
    col=1
    while col<ncol :
        print("columns: ",col)
        col+= 1
    row+=1 







    
    


