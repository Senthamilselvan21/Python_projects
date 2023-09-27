#Error program
if __name__ == '__main__':
    n = int(input("Enter no: "))
    student_marks = {}
    for _ in range(n):
        name, *line = input("Enter value:").split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    count=0
    value = student_marks.values()
    print(len(value))
    for v in range(0,len(value+1)):
        count=count+value[v]
    print(count)

