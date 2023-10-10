from tkinter import *

window = Tk()
window.title('Slider Pack')

def slide():
	my_label = Label(window, text=horizontal.get()).pack()
	#window.geometry(str(horizontal.get()) + "x" + str(vertical.get()))

vertical = Scale(window, from_=0, to=200)
vertical.pack()

horizontal = Scale(window, from_=0, to=400, orient=HORIZONTAL)
horizontal.pack()

my_btn = Button(window, text="Click Me!", command=slide).pack()

window.mainloop()
