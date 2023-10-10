u_list=[10,5.6,"Hello","apple"]
length=len(u_list)
print("Length=",length)
i=0
for j in range(1,length+1):
	print("Forward:[",i,"]:",u_list[i])
	print("Backwrd:[",-j,"]:",u_list[-j])
	i=i+1
