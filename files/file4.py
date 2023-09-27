f=open("file.txt","w") # writing a file if is already exits overwriting it or else create a new file
name="hi\n"
f.write(name)
f.write("Hello how are you\n")
f.write("""I'm fine thanks\n""")
f.close()
f=open("file.txt","r") # Reading mode used to view the contents in a file
content=f.readlines() # reads line by line
print(content)
for lines in content: # prints each line
    print(lines)
f.close()