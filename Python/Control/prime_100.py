range_value=int(input("Enter the range:"))
flag=0
prime_flag=0
for pnum in range(2,range_value):
	prime_flag= 0
	if flag<100:
		for num in range(1,pnum+1):
			if(pnum%num == 0):
				prime_flag=prime_flag+1
	if(prime_flag == 2):
	     print(flag," Num is::",pnum)
	     prime_flag= 0
	     flag=flag+1
				
