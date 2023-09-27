big_fun = lambda x,y:x  if x >= y else y
#big_fun = lambda x,y:[x if x>y else y] Output will be like:Biggest among two number :  [4]
x=int(input("Enter a number: "))
y=int(input("Enter a number: "))
big = big_fun(x,y)
print("Biggest among two number : ",big)

