import tkinter as tk
import gui
import db


class confirmationWindow(object):

    def yes(self):
        # Confirm the deletion of a contact.
        name = self.name

        gui.mainWindow(self.master).delete_contact(name)
        db.db_commit()
        self.top.destroy()

    def no(self):
        # Decline the deletion of a contact.
        gui.mainWindow(self.master)
        self.top.destroy()

    def __init__(self, master, name):
        top = self.top = tk.Toplevel(master)
        self.master = master
        self.name = name
        top.title('Confirm')

        self.label = tk.Label(top, text='''Are you sure you want to delete this contact?''')
        self.label.grid(row=0, column=1, padx=20, pady=10)

        self.yes_button = tk.Button(top, text='Yes', command=self.yes)
        self.yes_button.grid(row=1, column=1)

        self.no_button = tk.Button(top, text='No', command=self.no)
        self.no_button.grid(row=2, column=1, pady=10)
