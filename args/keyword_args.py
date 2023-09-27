# key word arguments(**kwargs)
def account_validation(**kwargs):
    for key in kwargs.keys():
        print("Key is : ", key)

    for value in kwargs.values():
        print("Values is: ", value)
    for key,value in kwargs.items():
        print("Keys with value", ":", key, ":", value)


account_validation(username="senthamil", phone=6374393823,email="ssenthamilselva21@gmail.com")
