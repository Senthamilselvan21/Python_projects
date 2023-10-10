# Different types of sets in Python
# set of integers
my_set_same = {1, 2, 3}
print(my_set_same)

# set of mixed datatypes
my_set_mix = {1.0, "Hello",100,'Hi' }
# printing the data from the set
# set unordered data so we can access using loop
print("************")
for num in my_set_mix:
    print(num)
print("************")
# set cannot have duplicates
# Output: {1, 2, 3, 4}
my_set_duplicate = {1, 2, 3, 4, 3, 2}
print(my_set_duplicate)
#Creating  set usig set function
my_set_by_set= set("123abc") 
print(my_set_by_set)

#Creating empty set

# Distinguish set and dictionary while creating empty set

# initialize a with {}
a = {}

# check data type of a
print(type(a))

# initialize a with set()
a = set()

# check data type of a
print(type(a))
