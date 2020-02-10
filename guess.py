#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""Guess a number between 1 and 10."""


import tkinter as tk
import tkinter.messagebox as msgbox
import tkinter.ttk as ttk

from random import randint


class GuessingGame(tk.Frame):
    """Play a guessing game."""

    def __init__(self, master=None):
        """Initialize the application."""
        super().__init__(master)
        self.master = master
        self.pack()
        # start the game with a clean slate
        self.losses = 0
        self.wins = 0
        # set up widgets
        self.create_widgets()

    def create_widgets(self):
        """Set up the widgets."""
        # add label text
        self.label = tk.Label(
            self,
            text="Choose A Number Between 1 and 10",
            font=("Arial Bold", 14),
        )
        # set label position
        self.label.grid(column=0, row=0)

        # add a textbox
        self.textbox = tk.Entry(self, width=5)
        # bind the return key
        self.textbox.bind("<Return>", (lambda event: self.submit()))
        # set textbox position
        self.textbox.grid(column=0, row=1)
        # focus the cursor in the textbox
        self.textbox.focus()

        # add a combobox
        self.combobox = ttk.Combobox(self, width=5)
        self.combobox["values"] = [i for i in range(1, 10 + 1)]
        # set default value blank
        self.combobox.current()
        # set combobox position
        self.combobox.grid(column=0, row=2)

        # add a spinbox
        self.spinbox = tk.Spinbox(self, from_=1, to=10, width=5)
        # set spinbox position
        self.spinbox.grid(column=0, row=3)

        # add a submit button
        self.submit_button = tk.Button(
            self,
            text="Submit",
            font=("Bold", 10),
            command=self.submit,
        )
        # set submit button position
        self.submit_button.grid(column=0, row=4)

        # add a quit button
        self.quit_button = tk.Button(
            self,
            text="Quit",
            font=("Bold", 10),
            command=self.master.destroy,
        )
        # set quit button position
        self.quit_button.grid(column=0, row=5)

    # add submit click event
    def submit(self):
        """Handle submit click event."""
        # get input from textbox
        guess = self.textbox.get()
        if len(guess) == 0:
            # if textbox is empty, get input from combobox
            guess = self.combobox.get()
            if len(guess) == 0:
                # if combobox is empty, get input from spinbox
                guess = self.spinbox.get()
        # convert guess string to integer
        if guess.isdigit():
            guess = int(guess)
        # pick a random number
        answer = randint(1, 10)

        # check the player's guess
        if guess == answer:
            self.losses = 0
            self.wins += 1
            title = "You Win!"
            msg = f"It was {guess}! You've won {self.wins} times!"
        else:
            self.losses += 1
            title = "You Lose!"
            if self.losses >= 3:
                msg = (
                    "It was "
                    + str(answer)
                    + "! You've lost "
                    + str(self.losses)
                    + " times in a row! Give up already!"
                )
            else:
                msg = f"Incorrect! It was {answer}!"
        # show pop-up messagebox
        msgbox.showinfo(title, msg)


def guessing_game():
    """Set up the guessing game."""
    # create the window
    root = tk.Tk()
    # create the application
    game = GuessingGame(master=root)
    # set the window title
    game.master.title("Guessing Game")
    # set window size
    game.master.geometry("360x180")
    # start the program
    game.mainloop()


if __name__ == "__main__":
    guessing_game()
