from tkinter import*

root = Tk()
#entry Widget
e = Entry(root, width=50, bg="#ddf79c", fg='#eb3d4e', borderwidth=5)
e.pack()
e.insert(0,'Enter you name here!!')
#only one box so 0

def myClick():
    Hello = "Hello!! "+e.get()
    # myLabel = Label(root, text=f'Hello! {e.get()}')
    myLabel = Label(root, text=Hello)

    myLabel.pack()

myButton = Button(root, text="Enter your name", command=myClick)
myButton.pack()

root.mainloop()