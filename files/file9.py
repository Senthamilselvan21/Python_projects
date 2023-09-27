filename=input("Enter file name: ")
try:
    f = open("file.txt","r")

    for lines in f:
        print(lines,end=" ")
        f.close()
except FileNotFoundError:
    print("File not Found")
except PermissionError:
    print("dont have the permission to read the file")
except FileExistsError:
    print("File is already existing")
except:
    print("Unexpected error while reading a file")
else:
    print("proigram run without any problem")
finally:
    print("finally: this will always execute")