number=int(input("Enter a number: "))
if number > 1:
    for i in range(2,number):
        if (number % i ) != 0:
            print(" Is a prime number")
            break
        elif (i % 2) == 0:
            print("Even number")
            break
        else:
            print("Is not  a prime number")
            break
else:
    print("Its not a prime number")
