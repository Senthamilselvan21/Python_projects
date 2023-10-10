'''Syntax:
	list_name[lower_index:upper_index]
'''
list1=[9,6,5,8,1,3,7,4]
 
print (list1)       #printing the complete list
 
print (list1[:-5])  #This will slice the elements from -5 to backward index
 
print (list1[-5:])  #This will slice the elements from -5 to forward index
 
print (list1[:5])   #This will slice the elements from 5 to backward index
 
print (list1[5:])   #This will slice the elements from 5 to forward index
 
print (list1[2:5])  #This willslice the elements in between 2:5
print (list1[-5:-2])  #This willslice the elements in between -5:-2
 
list1[2:5]=[11,12,44] #Modifying  the elements in between 2:5
 
print (list1)       #printing the complete list
