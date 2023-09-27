f=open("file.txt")
print(f.read(20)) # Reads only first 20 characters
print("***************")
print(f.read()) # prints remaining characters
f.close()