my_set_using_list = set(['one', 'two', 'nine', 33, 13])
my_set_using_tuple = set(("alpha", "beta", "gamma"))
print("set using list")
print(my_set_using_list)
print("set using tuple")
print (my_set_using_tuple)
# set cannot have mutable items
# here [3, 4] is a mutable list
# this will cause an error.

my_set = {1, 2, [3, 4]}
