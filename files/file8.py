with open("file.txt","w") as f:
    f.write("my first file\n")
    f.write("this is  file\n")
    f.write("that contains three lines\n")
    f.close()
with open("file.txt","r") as f:
    print(f.read())