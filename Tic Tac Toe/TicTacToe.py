from tkinter import *
import random

# ----------------------WHEN BUTTON PRESSED-------------------


def button_pressed(row, col):
    global player

    if button[row][col]['text'] == "" and check_winner() is False:
        if player == players[0]:
            button[row][col]['text'] = player

            if check_winner() is False:
                player = players[1]
                title_label.config(text=(player + " turn"))
            elif check_winner() is True:
                title_label.config(text=(player + " win's"))
            elif check_winner() == 'Tie':
                title_label.config(text=("Tie"))

        else:
            button[row][col]['text'] = player

            if check_winner() is False:
                player = players[0]
                title_label.config(text=(player + " turn"))
            elif check_winner() is True:
                title_label.config(text=(player + " win's"))
            elif check_winner() == 'Tie':
                title_label.config(text=("Tie"))


def check_winner():

    for row in range(3):
        if button[row][0]['text'] == button[row][1]['text'] == button[row][2]['text'] != "":
            button[row][0].config(bg='green')
            button[row][1].config(bg='green')
            button[row][2].config(bg='green')
            return True

    for column in range(3):
        if button[0][column]['text'] == button[1][column]['text'] == button[2][column]['text'] != "":
            button[0][column].config(bg='green')
            button[1][column].config(bg='green')
            button[2][column].config(bg='green')
            return True

    if button[0][0]['text'] == button[1][1]['text'] == button[2][2]['text'] != "":
        button[0][0].config(bg='green')
        button[1][1].config(bg='green')
        button[2][2].config(bg='green')
        return True

    elif button[0][2]['text'] == button[1][1]['text'] == button[2][0]['text'] != "":
        button[0][2].config(bg='green')
        button[1][1].config(bg='green')
        button[2][0].config(bg='green')
        return True

    elif empty_space() is False:
        for row in range(3):
            for col in range(3):
                button[row][col].config(bg='gray')
        return 'Tie'

    else:
        return False


def empty_space():

    for row in range(3):
        for col in range(3):
            if button[row][col]['text'] == "":
                return True
    return False


# --------------------CREATING WINDOW-----------------
window = Tk()
window.title("Tic-Tac-Toe")
window.iconphoto(False, PhotoImage(file='icon.png'))
window.geometry("500x500")

players = ['X', 'O']
player = random.choice(players)

title_label = Label(window, text=player + ' turn',
                    font=('Arial', 30), bg='magenta')
title_label.pack()


# ----------------------CREATING BUTTONS--------------------
button = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

button_frame = Frame(window)
button_frame.pack()

for row in range(3):
    for column in range(3):
        button[row][column] = Button(button_frame, text="", font=(
            'Arial, 30'), width=5, height=2, command=lambda row=row, column=column: button_pressed(row, column))
        button[row][column].grid(row=row, column=column, padx=1, pady=1)


window.mainloop()
