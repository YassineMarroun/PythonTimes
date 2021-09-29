from tkinter import *

root = Tk()

myFrame = Frame(root)
myFrame.pack()

resetScreen = False
operation = ""
result = 0


# ----------- Screen -----------

numberScreen = StringVar()

screen = Entry(myFrame, textvariable=numberScreen)
screen.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
screen.config(background="black", fg="#03f943", justify="right")


# ---------- Keystrokes ----------

def numberPressed(num):
    global resetScreen
    global operation
    
    if resetScreen != False:
        numberScreen.set(num)
        resetScreen = False
    else:
        numberScreen.set(numberScreen.get() + num)


# ---------- Function Sum ----------

def sum(num):
    global resetScreen
    global operation
    global result

    result += int(num)
    operation = "sum"
    resetScreen = True
    numberScreen.set(result)


# ---------- Function Subtraction ----------

num1 = 0
counter_sub = 0

def subtraction(num):
    global operation
    global result
    global num1
    global counter_sub
    global resetScreen

    if counter_sub == 0:
        num1 = int(num)
        result = num1
    else:
        if counter_sub == 1:
            result = num1 - int(num)
        else:
            result = int(result) - int(num)
        
        numberScreen.set(result)
        result = numberScreen.get()
    
    counter_sub = counter_sub + 1
    operation = "subtraction"
    resetScreen = True


# ---------- Function Multiplication ----------

counter_mult = 0

def multiplication(num):
    global operation
    global result
    global num1
    global counter_mult
    global resetScreen

    if counter_mult == 0:
        num1 = int(num)
        result = num1
    else:
        if counter_mult == 1:
            result = num1 * int(num)
        else:
            result = int(result) * int(num)
        
        numberScreen.set(result)
        result = numberScreen.get()
    
    counter_mult = counter_mult + 1
    operation = "multiplication"
    resetScreen = True


# ---------- Function Division ----------

counter_div = 0

def division(num):
    global operation
    global result
    global num1
    global counter_div
    global resetScreen

    if counter_div == 0:
        num1 = float(num)
        result = num1
    else:
        if counter_div == 1:
            result = num1 / float(num)
        else:
            result = float(result) / float(num)
        
        numberScreen.set(result)
        result = numberScreen.get()
    
    counter_div = counter_div + 1
    operation = "division"
    resetScreen = True

# ---------- Function the_result ----------

def the_result():
    global result
    global operation
    global counter_sub
    global counter_mult
    global counter_div
    
    if operation == "sum":
        numberScreen.set(result + int(numberScreen.get()))
        result = 0
    
    elif operation == "subtraction":
        numberScreen.set(result - int(numberScreen.get()))
        result = 0
        counter_sub = 0
    
    elif operation == "multiplication":
        numberScreen.set(result * int(numberScreen.get()))
        result = 0
        counter_mult = 0
    
    elif operation == "division":
        numberScreen.set(result / int(numberScreen.get()))
        result = 0
        counter_div = 0


# ----------- Row 1 -----------

button7 = Button(myFrame, text="7", width=3, command=lambda:numberPressed("7"))
button7.grid(row=2, column=1)
button8 = Button(myFrame, text="8", width=3, command=lambda:numberPressed("8"))
button8.grid(row=2, column=2)
button9 = Button(myFrame, text="9", width=3, command=lambda:numberPressed("9"))
button9.grid(row=2, column=3)
buttonDiv = Button(myFrame, text="/", width=3, command=lambda:division(numberScreen.get()))
buttonDiv.grid(row=2, column=4)


# ----------- Row 2 -----------

button4 = Button(myFrame, text="4", width=3, command=lambda:numberPressed("4"))
button4.grid(row=3, column=1)
button5 = Button(myFrame, text="5", width=3, command=lambda:numberPressed("5"))
button5.grid(row=3, column=2)
button6 = Button(myFrame, text="6", width=3, command=lambda:numberPressed("6"))
button6.grid(row=3, column=3)
buttonMult = Button(myFrame, text="x", width=3, command=lambda:multiplication(numberScreen.get()))
buttonMult.grid(row=3, column=4)


# ----------- Row 3 -----------

button1 = Button(myFrame, text="1", width=3, command=lambda:numberPressed("1"))
button1.grid(row=4, column=1)
button2 = Button(myFrame, text="2", width=3, command=lambda:numberPressed("2"))
button2.grid(row=4, column=2)
button3 = Button(myFrame, text="3", width=3, command=lambda:numberPressed("3"))
button3.grid(row=4, column=3)
buttonSub = Button(myFrame, text="-", width=3, command=lambda:subtraction(numberScreen.get()))
buttonSub.grid(row=4, column=4)


# ----------- Row 4 -----------

button0 = Button(myFrame, text="0", width=3, command=lambda:numberPressed("0"))
button0.grid(row=5, column=1)
buttonComma = Button(myFrame, text=",", width=3, command=lambda:numberPressed(","))
buttonComma.grid(row=5, column=2)
buttonEqual = Button(myFrame, text="=", width=3, command=lambda:the_result())
buttonEqual.grid(row=5, column=3)
buttonSum = Button(myFrame, text="+", width=3, command=lambda:sum(numberScreen.get()))
buttonSum.grid(row=5, column=4)


root.mainloop()