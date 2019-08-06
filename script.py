

import numpy as np
import sys
import os
scriptpath = "../imageEditor/AllModules.py"

# Add the directory containing your module to the Python path (wants absolute paths)
sys.path.append(os.path.abspath(scriptpath))
import time
from AllModules.py import open_image
from tkinter.messagebox import *

import cv2
from tkinter import *



mainWindow = Tk()
img = ImageTk.PhotoImage(Image.open("/media/yohan/NIKON D80/DCIM/100NCD80/DSC_5204.NEF"))
panel = tk.Label(root, image = img)
panel.pack(side = center, fill = "both", expand = "yes")
next = Button(text=">")
previous = Button(text="<")
next.pack(side=RIGHT)
def callback():
    if askyesno('Titre 1', 'Are you sure you want to move this file to trash'):
        showwarning('Titre 2', 'Tant pis...')
    else:
        showinfo('Titre 3', 'Vous avez peur!')
        showerror("Titre 4", "Aha")


mainWindow.mainloop()
