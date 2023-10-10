with open('file.txt', 'w') as f:
   f.write('my first file\n')
   f.write('This file\n')
   f.write('contains three lines\n')

with open('file.txt', 'r') as f:
   data=f.read()
   print (data)

