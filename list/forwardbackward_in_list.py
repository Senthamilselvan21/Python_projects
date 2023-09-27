"""my_list=[0,"hello",3.6,100,"google"]
length=len(my_list)
print("Forward Indexing")
for i in range(length):
    print(my_list[i])
print("negative indexing")
for i in range(1,length+1):
    print(my_list[-i])"""

u_list=[10,5.6,"Hello","apple"]
length=len(u_list)
print("Length ",length)
for i in range(length):
    print("Forward:[",i,"]:",u_list)
for j in range(1,length + 1):
    print("Backward:[",j,"]:",u_list[-j])