import tkinter as Tk


class confirmationWindow(object):

    def ok(self):
        self.top.destroy()

    def __init__(self, master):
        top = self.top = Tk.Toplevel(master)
        self.master = master
        top.title('404')

        self.label = Tk.Label(top, text='No Contact selected')
        self.label.grid(row=0, column=0, padx=10, pady=10)

        self.yes_button = Tk.Button(top, text='Ok', command=self.ok)
        self.yes_button.grid(row=1)
