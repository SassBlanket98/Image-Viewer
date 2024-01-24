import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

# Creating Window
window = Tk()
# Geometry of window
window.resizable()
# Title of window
window.title("David's Image Viewer")

frame = Frame(window, width = 230, height = 200, bg = "white")
frame.pack()

# Image list
# Open images
image1 = ImageTk.PhotoImage(Image.open("image1.jpg"))
image2 = ImageTk.PhotoImage(Image.open("image2.jpg"))
image3 = ImageTk.PhotoImage(Image.open("image3.jpg"))

# adding to list
lst = [image1, image2, image3]
i = 0
image_label = Label(frame, image = lst[i])
image_label.pack()

# Next image
def Next():
    global i
    i = i + 1
    try:
        image_label.config(image = lst[i])
    except:
        i = -1
        Next()

# Previous Image
def Back():
    global i
    i = i - 1
    try:
        image_label.config(image = lst[i])
    except:
        i = 0
        Back()

# Buttons
Button(window, text = "Back", command = Back, bg = "light blue").pack(side=LEFT, anchor=N)
Button(window, text = "Next", command = Next, bg = "light blue").pack(side=RIGHT, anchor=N)

window.mainloop()