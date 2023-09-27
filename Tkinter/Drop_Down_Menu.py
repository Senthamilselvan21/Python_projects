from tkinter import *
window =  Tk()
window.title("Drop down menu")
clicked=StringVar()

#Drop on boxes
options=[
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]
clicked.set(options[0])
def show():
    mylabel=Label(window,text=clicked.get()).grid(row=2,column=0)


#*Options is the other menu options. *is used for unpacking the container,as list type here.
drop=OptionMenu(window,clicked,*options)
drop.grid(row=0,column=0)

myButton = Button(window,text="Show selection",command=show).grid(row=1,column=0)
myButton1=Button(window,text='close',bg="red",command=window.destroy).grid(row=4,column=0)

window.mainloop()