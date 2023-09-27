from tkinter import *
from tkinter import messagebox

window=Tk()
window.title("Message Box")

#showinfo,showwarning,showerror,askquestion,askokcancel,askyesno

def popup():
    responce=messagebox.askyesno("This is my popup!","Hello world!")
    Label(window,text=responce).pack()
    if responce == 1:
        Label(window,text="You clicked yes!").pack()
    else:
        Label(window,text="You Clicked No!!").pack()

Button(window,text="Popup",command=popup).pack()
myButton1=Button(window,text='close',bg="red",command=window.destroy).pack(anchor=S)

mainloop()
