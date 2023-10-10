from tkinter import *

# Top level window
window = Tk()

window.title("Paned Window Tutorial")
window.geometry('350x200')

# Create a panedwindow
pane = PanedWindow(window, orient=VERTICAL)
pane.pack(fill=BOTH, expand=1)

# Add some label widgets on panedwindow
row1 = Label(pane, text="Row 1", bg="red")
pane.add(row1)

row2 = Label(pane, text="Row 2", bg="blue")
pane.add(row2)

row3 = Label(pane, text="Row 3", bg="orange")
pane.add(row3)

window.mainloop()
