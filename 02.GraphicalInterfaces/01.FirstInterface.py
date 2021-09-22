from tkinter import *

root = Tk()
root.title("Testing window")
# root.resizable(True, False)

# root.iconbitmap("cats.ico")
root.geometry("650x350")
root.config(bg="blue")

myFrame = Frame()
myFrame.pack(side="left", anchor="n")
# myFrame.pack(fill="x", expand=True)
myFrame.config(bg="red")
myFrame.config(width="650", height="350")
myFrame.config(bd=35)
myFrame.config(relief="groove")
myFrame.config(cursor="pirate")

root.mainloop()
