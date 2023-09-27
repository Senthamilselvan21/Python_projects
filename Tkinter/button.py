from tkinter import *
def messageshow():
    print("Hello World")

window=Tk()
window.title("Creating button")
button=Button(window,text="Submit",width=25,bg="Green",command=messageshow)
button1=Button(window,text="Close",width=25,bg="Red",command=window.destroy)
button.grid()
button1.grid(row=1)
mainloop()


