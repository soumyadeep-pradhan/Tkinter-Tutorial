from tkinter import *

root = Tk()
#Creating  a label Widget
myLabel1 = Label(root, text = "Hello World!")
myLabel2 = Label(root, text = "My name is Soumyadeep")
myLabel3 = Label(root, text = "               ")
#shoving it onto the screen

myLabel1.grid(row= 0, column=0)
myLabel2.grid(row=1, column=10)
myLabel3.grid(row=1, column=1)

# object oriented
myLabel01 = Label(root, text = "Hi").grid(row=5, column=5)
myLabel02 = Label(root, text = "tkinter").grid(row=4, column=7)

root.mainloop()