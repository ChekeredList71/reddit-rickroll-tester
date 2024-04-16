# Import Module
import tkinter
from tkinter import *

# create root window
root = Tk()

# root window title and dimension
root.title("A Rickroll teszter")
# Set geometry (widthxheight)
root.geometry('350x200')

cim = Label(root, text="Kérlek add meg a linket!")

link = Entry(root, width=30)


def benne_van():
    top1 = Toplevel(root)
    top1.title = "A Rickroll eredménye"
    Label(text="A videó nem biztonságos!")

    def close_eredmeny():
        top1.destroy()
        top1.update()

    gomb1 = Button(text="vissza", command=close_eredmeny)

# ide kell majd a link utáni válasz


def nincs_benne():
    top1 = Toplevel(root)
    top1.title = "A Rickroll eredménye"
    Label(text="A videó teljesen biztonságos!")

    def close_eredmeny():
        top1.destroy()
        top1.update()

    gomb1 = Button(text="vissza", command=close_eredmeny)


gomb = Button(root, text="Kész", command=tkinter.Toplevel)

cim.pack(fill=X, padx=20)
link.pack(fill=X, padx=20)
gomb.pack(fill=X, padx=20)

# all widgets will be here
# Execute Tkinter
root.mainloop()
