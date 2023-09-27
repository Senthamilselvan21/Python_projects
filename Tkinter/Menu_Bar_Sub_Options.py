from tkinter import *

#Top level window
window=Tk()

window.title("Menu Bar sub Options Tutorial")
window.geometry("350x200")

#create a toplevel menu bar
menubar=Menu(window)

#Create file pulldown menus
filemenu=Menu(menubar,tearoff=1)
filemenu.add_command(label="Open")
filemenu.add_command(label="Save")
filemenu.add_separator()
filemenu.add_command(label="Exit",command=window.quit)
menubar.add_cascade(label="File",menu=filemenu)

#create edit pulldown menus
editmenu=Menu(menubar,tearoff=0)
editmenu.add_command(label="Cut")
editmenu.add_command(label="Copy")
editmenu.add_command(label="paste")
menubar.add_cascade(label="Edit",menu=editmenu)

#create help pulldown menu

helpmenu=Menu(menubar,tearoff=0)
helpmenu.add_command(label="About")
menubar.add_cascade(label="Help",menu=helpmenu)

#display the menu
window.config(menu=menubar)

window.mainloop()



