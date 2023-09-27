n = int(input("a :"))
arr = map(int, input().split())
l=[]
for i in arr:
    l.append(i)
    print(i ,end=" ")

maximum = max(l)
while max(l) == maximum:
    l.remove(max(l))
    pass
print('\n',max(l))