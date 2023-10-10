import functools 
import operator 
lis = [ 1 , 3, 5, 6, 2, ] 
print ("The sum of the list elements is : ",end="") 
print (functools.reduce(operator.add,lis)) 
print ("The product of list elements is : ",end="") 
print (functools.reduce(operator.mul,lis)) 
print ("The concatenated product is : ",end="") 
print (functools.reduce(operator.add,["geeks","for","geeks"]))
