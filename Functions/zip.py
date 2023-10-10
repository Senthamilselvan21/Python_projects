
# Python code to demonstrate the working of  
# zip() 
  
# initializing lists 
name = [ "Manjeet", "Nikhil", "Shambhavi", "Astha","manoj" ] 
roll_no = [ 4, 1, 3, 2 ,9] 
marks = [ 40, 50, 60, 70 ] 
  
# using zip() to map values 
mapped = zip(name, roll_no, marks) 
# converting values to print as set 
mapped = list(mapped) 
  
# printing resultant values  
print ("The zipped result is : ") 
#print ("The zipped result is : ") 
print (mapped) 
