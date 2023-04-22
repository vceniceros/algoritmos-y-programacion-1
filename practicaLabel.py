from tkinter import *

root=Tk()

miFrame = Frame(root, width=500, height=400)

miFrame.pack()

miLabel = Label(miFrame, text="Esto es bocaaa",fg="yellow", bg="blue",font=("Comic Sans MS",18)).place(x=100,y=200)

root.mainloop()