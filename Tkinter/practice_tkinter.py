from tkinter import *
window = Tk()
window.title("Practice GUI")
Label(window,text="First Name").grid(row=0)
Label(window,text="Last Name").grid(row=1)
Label(window,text="Course").grid(row=2)
Label(window,text="Stream").grid(row=3)
first=Entry(window)
second=Entry(window)
third=Entry(window)
fourth=Entry(window)
first.grid(row=0,column=1)
second.grid(row=1,column=1)
third.grid(row=2,column=1)
fourth.grid(row=3,column=1)
# Buttons
def user_input():
    print("Hello World!!")
button=Button(window,text="Submit",width=12,bg="green",command=user_input)
button1=Button(window,text="Close",width=12,bg="red",command=window.destroy)
button.grid(row=5,column=1)
button1.grid(row=5,column=2)

"""#Checklist

var1=IntVar()
var2=IntVar()
var3=IntVar()

def clicked(value):
    label=Label(window,text=value)
    label.pack()
    print(label)

Checkbutton(window,text="2021",variable=var1,command=lambda :clicked(var1.get())).pack(anchor="center")
Checkbutton(window,text="2022",variable=var2,command=lambda :clicked(var2.get())).pack(anchor="center")
Checkbutton(window,text="2023",variable=var3,command=lambda :clicked(var3.get())).pack(anchor="center")"""
mainloop()
