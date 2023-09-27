or_list=["fruits","veggies","dry","a"] #created list with strings
or_list1=[1,2,3]
or_list2=["a","b","c"]
print(or_list)
or_list.append(5) # added the element at end of the list as number
print(or_list)
or_list.append("sports") #added the element at end of the list as number
print(or_list)
or_list.insert(3,5.6) # insert number at the particular index
print(or_list)
or_list.insert(1,"start") #insert number at the particular index
print(or_list)
print(or_list1)
print(or_list2)
or_list1.extend(or_list2) # Merge two list into a single list
print(or_list1)
or_list.remove("a") # remove a data from a list  based on the input
print(or_list)
#or_list.remove(6)
#print (or_list)
print("Last element is",or_list.pop()) # removes always last data in the list
print(or_list)
print("2ND Index element is",or_list.pop(2)) #removes data for the particular index
print(or_list)
or_list.clear() #clears all the data and gives a empty list
print(or_list)

