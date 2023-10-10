or_list=["fruits","veggies","dry","a"] #created list with strings
or_list1=[1,2,3]
or_list2=["a","b","c"]
print (or_list)
or_list.append(5)       #added the element at end of the list as number
print (or_list)
or_list.append("sports") #added the element at end of the list as string
print(or_list)
or_list.insert(3,5.6)
print (or_list)
or_list.insert(1,'start')
print (or_list)
print (or_list1)
print (or_list2)
or_list1.extend(or_list2)
print (or_list1)
or_list.remove("a")
print (or_list)
#or_list.remove(6)
#print (or_list)
print("Last element is",or_list.pop())
print (or_list)
print ("1st element is",or_list.pop(2))
print (or_list)
or_list.clear()
print (or_list)
