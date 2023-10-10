'''Syntax:
	string_name[lower_index:upper_index]
'''
string = "python"
print (string[:])#python
print (string[1:])#ython
print (string[3:])#hon
print (string[:1])#p
print (string[:3])#pyt
print (string[0:3])#pyt
print (string[2:5])#tho
print (string[2:len(string)+5])#thon
print (string[:-1])#pytho
print (string[-1:])#n
print (string[-3:-1])#ho
print (string[-1:-3])#invalid
