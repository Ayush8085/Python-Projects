from tkinter import *

# -------------------FUNCTION FOR BUTTON PRESS----------------


def button_pressed(num):
    global text

    text = text + str(num)
    space.set(text)


def clear():

    global text
    text = ""
    space.set(text)


def equal():

    global text

    try:
        total = str(eval(text))
        space.set(total)
        text = total
    except ZeroDivisionError:
        space.set("arithmetic error")
        text = ""
    except SyntaxError:
        space.set("syntax error")
        text = ""


# -------------------WINDOW CREATION---------------
window = Tk()
window.iconphoto(False, PhotoImage(file='calculator_icon.ico'))
window.geometry("420x500")
window.title("Calculator")

# --------------------TEXT SPACE------------------
text = ""

space = StringVar()
label = Label(window, textvariable=space,
              font="Quicksand 35", width=13, bg='white')
label.pack()

frame = Frame(window)
frame.pack()

# ---------------------BUTTONS-------------------
b1 = Button(frame, text=1, font=35, height=3, width=6,
            command=lambda: button_pressed(1))
b1.grid(row=0, column=0)

b2 = Button(frame, text=2, font=35, height=3, width=6,
            command=lambda: button_pressed(2))
b2.grid(row=0, column=1, padx=8, pady=8)

b3 = Button(frame, text=3, font=35, height=3, width=6,
            command=lambda: button_pressed(3))
b3.grid(row=0, column=2)

b4 = Button(frame, text=4, font=35, height=3, width=6,
            command=lambda: button_pressed(4))
b4.grid(row=1, column=0)

b5 = Button(frame, text=5, font=35, height=3, width=6,
            command=lambda: button_pressed(5))
b5.grid(row=1, column=1, padx=8)

b6 = Button(frame, text=6, font=35, height=3, width=6,
            command=lambda: button_pressed(6))
b6.grid(row=1, column=2)

b7 = Button(frame, text=7, font=35, height=3, width=6,
            command=lambda: button_pressed(7))
b7.grid(row=2, column=0)

b8 = Button(frame, text=8, font=35, height=3, width=6,
            command=lambda: button_pressed(8))
b8.grid(row=2, column=1, padx=8, pady=8)

b9 = Button(frame, text=9, font=35, height=3, width=6,
            command=lambda: button_pressed(9))
b9.grid(row=2, column=2)

b0 = Button(frame, text=0, font=35, height=3, width=6,
            command=lambda: button_pressed(0))
b0.grid(row=3, column=0)

plus = Button(frame, text='+', font=35, height=3, width=6,
              command=lambda: button_pressed('+'))
plus.grid(row=0, column=3, padx=8, pady=8)

minus = Button(frame, text='-', font=35, height=3, width=6,
               command=lambda: button_pressed('-'))
minus.grid(row=1, column=3)

mul = Button(frame, text='*', font=35, height=3, width=6,
             command=lambda: button_pressed('*'))
mul.grid(row=2, column=3)

divide = Button(frame, text='/', font=35, height=3, width=6,
                command=lambda: button_pressed('/'))
divide.grid(row=3, column=3)

equal = Button(frame, text='=', font=35, height=3, width=6, command=equal)
equal.grid(row=3, column=2)

dot = Button(frame, text='.', font=35, height=3, width=6,
             command=lambda: button_pressed('.'))
dot.grid(row=3, column=1)

clear = Button(window, text='clear', font=50,
               height=3, width=10, command=clear)
clear.pack()


window.mainloop()
