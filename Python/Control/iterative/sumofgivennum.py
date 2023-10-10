num=int(input("enter a number:"))
sumn=0
rem=0
while num>0:
	rem=num%10
	sumn=sumn+rem
	num=num//10
print ("sum of given num is:",sumn	)
