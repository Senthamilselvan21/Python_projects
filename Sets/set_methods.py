my_set = {4, 1, 9, 6}
print (my_set)
# add an element
my_set.add(7)
print (my_set)
# remove an element
my_set.remove(1)
print (my_set)
# update an element
my_set.update([33, 44])
print (my_set)
#discard an element
my_set.discard(4)
print(my_set)
# pop random element
my_set.pop()
print(my_set)
print("max is:",max(my_set))
print("min is:",min(my_set))
print("sum is:",sum(my_set))
print("len is:",len(my_set))
my_set.update(('a', 'b'))
print (my_set)
my_set.clear()
print (my_set)
