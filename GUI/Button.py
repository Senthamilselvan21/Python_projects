from  tkinter import *
def messageshow():
    print("Hello World")

window = Tk()
window.title('Creating a Button')
#button =Button(window, text='Submit', width=25, command=window.destroy)
button =Button(window, text='Submit', width=25, command=messageshow)
button.pack()
mainloop()

