  
from tkinter import *
from tkinter import messagebox

window = Tk()
window.title('Message Box')

# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno

def popup():
	response = messagebox.askyesno("This is my Popup!", "Hello World!")
	Label(window, text=response).pack()
	if response == 1:
		Label(window, text="You Clicked yes!").pack()
	else:
		Label(window, text="You Clicked No!!").pack()

Button(window, text="Popup", command=popup).pack()



mainloop()
