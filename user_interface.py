# Import Module
from tkinter import *

# create root window
root = Tk()

# root window title and dimension
root.title("A Rickroll teszter")
# Set geometry (widthxheight)
root.geometry('350x200')

cim = Label(root, text="Kérlek add meg a linket!")
cim.grid(column=3, row=1)

link = Entry(root, width=10)
link.grid(column=3, row=2)

# ide kell majd a link utáni válasz

gomb = Button(root, text="Kész")
gomb.grid(column=3, row=3)

# all widgets will be here
# Execute Tkinter
root.mainloop()
