glo_var=50 
def fun(): 
   loc_var=40 
   glo_var=530 
   print ("Inside Fun:Global variable is:",glo_var) 
   print ("Inside Fun: Local variable is:",loc_var) 
fun() 
print ("Outside Fun:Global variable is:",glo_var)
print ("Outside Fun: Local variable is:",loc_var) 
