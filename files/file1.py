"""
open(filename,mode)
"""
#file_obj=open("//Desktop//Python practice/)"

file_obj=open("dec_to_bin.txt")
print("File name: ",file_obj.name) #returns name of the file
print("File State: ",file_obj.closed) # returns file status whether is closed or not
print("Opening mode: ",file_obj.mode) # retuns the mode of the file 
print(file_obj.read())
file_obj.close()
print("File state: ",file_obj.closed)
