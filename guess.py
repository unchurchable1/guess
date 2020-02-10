#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""Guess a number between 1 and 10."""


import tkinter as tk
import tkinter.messagebox as msgbox
import tkinter.ttk as ttk

from random import randint


class GuessingGame:
    """Play a guessing game."""

    def __init__(self):
        """Initialize the window."""
        # start the game with a clean slate
        self.__losses = 0
        self.__wins = 0
        # create the window
        self.__window = tk.Tk()
        # set the window title
        self.__window.title("Guessing Game")
        # set window size
        self.__window.geometry("360x180")
        # set up widgets
        self.create_widgets()

    def create_widgets(self):
        """Set up the widgets."""
        # add label text
        self.__label = tk.Label(
            self.__window,
            text="Choose A Number Between 1 and 10",
            font=("Arial Bold", 14),
        )
        # set label position
        self.__label.grid(column=0, row=0)

        # add a textbox
        self.__textbox = tk.Entry(self.__window, width=5)
        # bind the return key
        self.__textbox.bind("<Return>", (lambda event: self.submit()))
        # set textbox position
        self.__textbox.grid(column=0, row=1)
        # focus the cursor in the textbox
        self.__textbox.focus()

        # add a combobox
        self.__combobox = ttk.Combobox(self.__window, width=5)
        self.__combobox["values"] = [i for i in range(1, 10 + 1)]
        # set default value blank
        self.__combobox.current()
        # set combobox position
        self.__combobox.grid(column=0, row=2)

        # add a spinbox
        self.__spinbox = tk.Spinbox(self.__window, from_=1, to=10, width=5)
        # set spinbox position
        self.__spinbox.grid(column=0, row=3)

        # add a submit button
        self.__submit = tk.Button(
            self.__window,
            text="Submit",
            font=("Bold", 10),
            command=self.submit,
        )
        # set submit button position
        self.__submit.grid(column=0, row=4)

        # add a quit button
        self.__quit = tk.Button(
            self.__window,
            text="Quit",
            font=("Bold", 10),
            command=self.__window.destroy,
        )
        # set quit button position
        self.__quit.grid(column=0, row=5)

    # add submit click event
    def submit(self):
        """Handle submit click event."""
        # get input from textbox
        guess = self.__textbox.get()
        if len(guess) == 0:
            # if textbox is empty, get input from combobox
            guess = self.__combobox.get()
            if len(guess) == 0:
                # if combobox is empty, get input from spinbox
                guess = self.__spinbox.get()
        # convert guess string to integer
        if guess.isdigit():
            guess = int(guess)
        # pick a random number
        answer = randint(1, 10)

        # check the player's guess
        if guess == answer:
            self.__losses = 0
            self.__wins += 1
            title = "You Win!"
            msg = f"It was {guess}! You've won {self.__wins} times!"
        else:
            self.__losses += 1
            title = "You Lose!"
            if self.__losses >= 3:
                msg = (
                    "It was "
                    + str(answer)
                    + "! You've lost "
                    + str(self.__losses)
                    + " times in a row! Give up already!"
                )
            else:
                msg = f"Incorrect! It was {answer}!"
        # show pop-up messagebox
        msgbox.showinfo(title, msg)

    def start(self):
        """Start the main window loop."""
        self.__window.mainloop()


if __name__ == "__main__":
    GuessingGame().start()
