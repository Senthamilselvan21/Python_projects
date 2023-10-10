from tkinter import *

# Top level window
window = Tk()

window.title("Spin Box Tutorial")
window.geometry('350x200')

# Create a spinbox
spinbox = Spinbox(window, from_=1, to=10)
spinbox.pack()

window.mainloop()
