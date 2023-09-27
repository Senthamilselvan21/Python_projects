"""def test_var_args(f_arg,*argv):
    print("first normal arg : ",f_arg)
    for arg in argv:
        print("another arg through *argv : ",arg)
test_var_args('yasoob','python','eggs','test')"""

def attendence(first,*login):
    print("The member who logged first : ",first)
    for members in login:
        print("The remaining persons: ",members)
attendence("senthil","ramu","karthick")
        
