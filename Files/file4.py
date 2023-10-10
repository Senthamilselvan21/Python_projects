f=open('file.txt', 'w')
name="besant\n"
f.write(name)
f.write('Hi how are you\n')
f.write('fine whats going on\n')
f.close()
f= open('file.txt', 'r')
content = f.readlines()
for line in content:
    print(line)
    
f.close()
