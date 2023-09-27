from tkinter import *
window = Tk()
window.title("Check box Tutorial")
varReg=IntVar()
varEniq=IntVar()
def clicked(value):
    mylabel=Label(window,text=value)
    mylabel.pack()
    print(value)

Checkbutton(window,text="Regestration",variable=varReg,command=lambda:clicked(varReg.get())).pack(anchor=W) #w denotes direction
Checkbutton(window,text="Enquiry",variable=varEniq,command=lambda:clicked(varEniq.get())).pack(anchor=W)
mainloop()