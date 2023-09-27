from tkinter import *
window = Tk()
Label(window,text="Username").grid(row=0)
Label(window,text="Password").grid(row=1)
first=Entry(window)
second=Entry(window)
first.grid(row=0,column=1)
second.grid(row=1,column=1)
mainloop()
