with open("sample.txt","w",) as f:
    f.write("Raman")
with open("sample.txt","a") as f:
    f.write("\t This is the appending line")
with open("sample.txt","r") as f:
    o = f.read()
print(o)
f.close()