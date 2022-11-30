from tkinter import *
from tkinter import colorchooser
from tkinter import font
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.messagebox import showinfo
import os

# ------------------------COMMAND FUNCTIONS-------------------------


def new_file():
    window.title('Untitled')
    text_area.delete(1.0, END)


def open_file():
    file = askopenfilename(defaultextension=".txt", file=[
                           ('All Files', '*.*'), ("Text Documents", "*.txt")])

    if file == "":
        file = None
    else:
        window.title(os.path.basename(file) + " - Text Editor")
        text_area.delete(1.0, END)
        f = open(file, 'r')
        text_area.insert(1.0, f.read())
        f.close()


def save_file():
    global file
    if file == None:
        file = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt", file=[
                                 ('All Files', '*.*'), ("Text Documents", "*.txt")])

        if file == '':
            file = None
        else:
            f = open(file, 'w')
            f.write(text_area.get(1.0, END))
            f.close()

            window.title(os.path.basename(file) + ' - Text Editor')
    else:
        f = open(file, 'w')
        f.write(text_area.get(1.0, END))
        f.close()

        window.title(os.path.basename(file) + ' - Text Editor')


def exit_program():
    window.destroy()


def cut():
    text_area.event_generate(('<<Cut>>'))


def copy():
    text_area.event_generate(('<<Copy>>'))


def paste():
    text_area.event_generate(('<<Paste>>'))


def font_color():
    color = colorchooser.askcolor(title="Pick your color")
    # print(color)
    text_area.config(fg=color[1])


def about():
    showinfo(title="The Author: ",
             message="This project is made by Ayush Kumar Tiwari")


# -----------------CREATING WINDOW----------------
window = Tk()
window.title("Untitled - Text Editor")
window.iconphoto(False, PhotoImage(file='icon.png'))
window.geometry("700x500")

# ---------------------TEXT AREA------------------
text_area = Text(window, font=('Arial 15'))
text_area.pack(expand=True, fill=BOTH)

file = None
# -----------------------CREATING THE MENU BAR-----------------------
menu_bar = Menu(window)

# --------------------FILE MENU--------------------
file_menu = Menu(menu_bar, tearoff=0)

file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_program)

menu_bar.add_cascade(label='File', menu=file_menu)

# ----------------------EDIT MENU------------------
edit_menu = Menu(menu_bar, tearoff=0)

edit_menu.add_command(label="Cut", command=cut)
edit_menu.add_command(label="Copy", command=copy)
edit_menu.add_command(label="Paste", command=paste)
edit_menu.add_command(label="Font Color", command=font_color)

menu_bar.add_cascade(label="Edit", menu=edit_menu)

# ----------------------HELP MENU------------------
help_menu = Menu(menu_bar, tearoff=0)

help_menu.add_command(label='About', command=about)

menu_bar.add_cascade(label='Help', menu=help_menu)


# -----------------------SCROLL BAR-------------------
scroll_bar = Scrollbar(text_area)
scroll_bar.pack(side=RIGHT, fill=Y)
scroll_bar.config(command=text_area.yview)
text_area.config(yscrollcommand=scroll_bar.set)


window.config(menu=menu_bar)

window.mainloop()
