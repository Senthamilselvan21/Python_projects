"""
syntax: list_name[lower_index/start_index:upper_index/stop_index]
"""
list1=[9,6,5,8,1,3,7,4]
print(list1)
print(list1[:-5])
print(list1[-5:])
print(list1[:5])
print(list1[5:])
print(list1[2:5])
print(list1[-5:-2])
list1[2:5] = [11,12,44] #Difference between string and list in slicing

print(list1)
