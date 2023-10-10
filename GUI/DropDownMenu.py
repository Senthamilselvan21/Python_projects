from tkinter import *
window = Tk()
window.title('Drop Down Menu')



clicked = StringVar()

# Drop Down Boxes
options = [
	"Monday", 
	"Tuesday", 
	"Wednesday", 
	"Thursday", 
	"Friday",
	"Saturday"
]
clicked.set(options[0])
def show():
	myLabel = Label(window, text=clicked.get()).grid(row=2,column=0)

# *Options is the other menu options. * is used for unpacking the container, as list type here.
drop = OptionMenu(window, clicked, *options)
drop.grid(row=0,column=0)

myButton = Button(window, text="Show Selection", command=show).grid(row=1,column=0)

window.mainloop()
