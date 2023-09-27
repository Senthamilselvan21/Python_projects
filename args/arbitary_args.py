def greet(*names):
    """
    this function greets all the persons in the names tuple
    """
    #names in tuple with arguments
    for name in names:
        print("Hello",name)
greet("muniraj", "raman", "rahul", "vishwa")
