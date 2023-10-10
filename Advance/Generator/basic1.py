def print_odd(data) :
    print("fun")
    for x in data:
      if x % 2 == 1:
         yield x
 
data = [1, 4, 5, 6, 7]
print ("The odd numbers in list are : ")
 
for i in print_odd(data):
 
    print (i,end="\n")
 
print("\n")
