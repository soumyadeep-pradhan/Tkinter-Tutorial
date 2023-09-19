from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text="Look! I clicked a button")
    myLabel.pack()
# myButton = Button(root, text="Click Me!",state=DISABLED)
# myButton = Button(root, text="Click Me!",padx=10,pady=50)
myButton = Button(root, text="Click Me!",command=myClick,fg="yellow",bg="black")# foreground and backgroundcolor

myButton.pack()

root.mainloop()