import tkinter as tk


class confirmationWindow(object):

    def ok(self):
        self.top.destroy()

    def __init__(self, master):
        top = self.top = tk.Toplevel(master)
        self.master = master
        top.title('400')

        self.label = tk.Label(top, text='Address Book Name must contain at least 3 characters')
        self.label.grid(row=0, column=0, padx=10, pady=10)

        self.yes_button = tk.Button(top, text='Ok', command=self.ok)
        self.yes_button.grid(row=1)
