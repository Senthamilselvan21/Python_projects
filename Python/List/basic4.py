or_list1 =[1,2,3,4]
or_list2 =[1.2,2.5,3.6,4.3]
print (or_list1)
print (or_list2)
del or_list1[0] #delete first element
print (or_list1)
del or_list1[:] #delete complete list
print (or_list1)
del or_list2[0:3] #delete element between 0,1
print (or_list2)
del or_list2[0:len(or_list2)] #delete complete list
print (or_list2)
del or_list1
del or_list2
print (or_list2)
