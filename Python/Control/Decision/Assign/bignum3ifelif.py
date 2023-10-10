a=int(input("enter a first num:"))
b=int(input("enter a second num:"))
c=int(input("enter a third num:"))
if a>b and a>c:
	print ("a is big:",a)
elif b>a and b>c:
	print ("b is big:",b)
elif c>a and c>b:
	print ("c is big:",c)
else:
	print ("two or three nums are same")

