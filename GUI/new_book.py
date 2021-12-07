import tkinter as tk
from tkinter import ttk
import sys
import db
import gui
import new_book_cw


class addNewBookWindow(object):

    def ok(self):
        # Open the specified address book.
        book_name = self.book_name.get()

        if len(book_name) > 2:
            db.db_init(book_name)
            root = tk.Tk()
            self.master.withdraw()
            root.protocol("WM_DELETE_WINDOW", exit)
            root.geometry('600x600')
            gui.mainWindow(root)
            root.mainloop()
            sys.exit()

        else:
            self.c = new_book_cw.confirmationWindow(self.master)

    def close_window(self):
        self.master.destroy()

    def __init__(self, master):
        self.master = master

        # UI options
        paddings = {'padx': 2, 'pady': 10}

        # configure the grid
        master.columnconfigure(0, weight=1)
        master.columnconfigure(1, weight=3)

        self.instruction_message = tk.Label(self.master, font='arial 12 bold', text='Enter The Name Of Your New Address Book')
        self.instruction_message.grid(**paddings)

        # Book Name
        self.book_name_label = tk.Label(self.master, font='arial 12', text='Address Book Name:')
        self.book_name_label.grid(row=1, sticky=tk.W, **paddings)

        self.book_name = tk.Entry(self.master, font='arial 12')
        self.book_name.grid(row=1, ipady=5, ipadx=30, sticky=tk.E, **paddings)

        self.cancel_button = tk.Button(self.master, bg='red', font='arial 12', text='Cancel', command=self.close_window)
        self.cancel_button.grid(row=2, **paddings)

        self.ok_button = tk.Button(self.master, font='arial 12', text='Ok', command=self.ok)
        self.ok_button.grid(row=2, sticky=tk.E, padx=20)
