def SquareOfNums():
 
    x = 1;
 
    while True:
 
        yield x*x
 
        x += 1
 
for num in SquareOfNums():
 
    if num > 32:
 
        break
 
    print("num is:",num)
