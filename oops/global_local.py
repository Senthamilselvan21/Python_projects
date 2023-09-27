def fun1():
    global x
    x = 10

    def func2():

        x = 20
        print("X value inside fun: ",x)
    func2()
    print(x)
fun1()
print(x)
