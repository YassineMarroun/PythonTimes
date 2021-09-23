from tkinter import *

root = Tk()

myFrame = Frame(root, width=1200, height=600)
myFrame.pack()

myName = StringVar()

# Text boxes

textName = Entry(myFrame, textvariable=myName)
textName.grid(row=0, column=1, padx=10, pady=10)
textName.config(fg="red", justify="center")

textPassword = Entry(myFrame)
textPassword.grid(row=1, column=1, padx=10, pady=10)
textPassword.config(show="*")

textSurname = Entry(myFrame)
textSurname.grid(row=2, column=1, padx=10, pady=10)

textAddress = Entry(myFrame)
textAddress.grid(row=3, column=1, padx=10, pady=10)

textComments = Text(myFrame, width=16, height=5)
textComments.grid(row=4, column=1, padx=10, pady=10)


# Scrollbar

scrollVert = Scrollbar(myFrame, command=textComments.yview)
scrollVert.grid(row=4, column=2, sticky="nsew")
textComments.config(yscrollcommand=scrollVert.set)


# Labels

nameLabel = Label(myFrame, text="Name: ")
nameLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)

passwordLabel = Label(myFrame, text="Password: ")
passwordLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)

surnameLabel = Label(myFrame, text="Surname: ")
surnameLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)

addressLabel = Label(myFrame, text="Address: ")
addressLabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)

commentsLabel = Label(myFrame, text="Comments: ")
commentsLabel.grid(row=4, column=0, sticky="e", padx=10, pady=10)


# Buttons

def codeButton():
    myName.set("Yassine")

submitButton = Button(root, text="Submit", command=codeButton)
submitButton.pack()


root.mainloop()