'''
open(filename,mode)
'''
#file_obj=open("//home//hakeem//Hakeem//Training//Python//Files//sample.txt")

file_obj = open("sample.txt")
print ("File name: ", file_obj.name)
print ("File state: ", file_obj.closed)
print ("Opening mode: ", file_obj.mode)
file_obj.close()
