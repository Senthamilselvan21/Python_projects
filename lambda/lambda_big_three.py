big_fun = lambda x,y,z: max(x,max(y,z))
#big_fun = lambda x,y:[x if x>y else y] Output will be like:Biggest among two number :  [4]
x=int(input("Enter a number: "))
y=int(input("Enter a number: "))
z=int(input("Enter a number: "))
big = big_fun(x,y,z)
print("Biggest among three number : ",big)