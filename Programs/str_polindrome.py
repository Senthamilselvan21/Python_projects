# change this value for a different output
my_str = input("Enter a string:")

# make it suitable for caseless comparison
#my_str = my_str.casefold()

# reverse the string
#rev_str = reversed(my_str)

# check if the string is equal to its reverse
if my_str == my_str[::-1]:
   print("It is palindrome")
else:
   print("It is not palindrome")
