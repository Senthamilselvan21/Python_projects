A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
print("Set Union")
# use | operator
# Output: {1, 2, 3, 4, 5, 6, 7, 8}
print(A | B)
# use union function
print(A.union(B))
# use union function on B
print(B.union(A))
# use & operator
# Output: {4, 5}
print(A & B)
# use intersection function on A
print(A.intersection(B))

# use intersection function on B
print(B.intersection(A))

# use - operator on A
# Output: {1, 2, 3}
print(A - B)

# use difference function on A
print(A.difference(B))

# use - operator on B
print(B - A)

# use difference function on B
print(B.difference(A))

# use ^ operator
# Output: {1, 2, 3, 6, 7, 8}
print(A ^ B)

# use symmetric_difference function on A
print(A.symmetric_difference(B))

# use symmetric_difference function on B
print(B.symmetric_difference(A))


