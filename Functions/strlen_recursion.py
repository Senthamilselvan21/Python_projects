str = "samarth"
def recLen(i) : 
  
#    global str
      
    if (i == len(str)) : 
        return 0
    else : 
        return 1 + recLen(i + 1)  
      
print (recLen(0)) 
  
