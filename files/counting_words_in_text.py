f = open("sample.txt","w")
s = "Hi hello how are you "
f.writelines(s)
f.close()

with open("sample.txt","r") as f:
    lines = f.read()
text = lines.split()
count = 0
for i in text:
    count=count+len(i)
print("Number of words in a text is : ",count)