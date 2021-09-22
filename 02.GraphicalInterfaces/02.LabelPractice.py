from tkinter import *

root = Tk()

myFrame = Frame(root, width=500, height=400)
myFrame.pack()

# myImage = PhotoImage(file="mouse.gif")
# Label(myFrame, image=myImage).place(x=100, y=200)
Label(myFrame, text="Using Label in Frame", fg="red", font=("Comic Sans MS", 18)).place(x=100, y=200)

root.mainloop()