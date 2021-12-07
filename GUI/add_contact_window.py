import tkinter as tk
import functions
import gui
import add_confirmation_window as cw


class newContactWindow(object):

    def close_window(self):
        self.top.destroy()

    def field_return(self):
        # List to hold form data
        field_list = [' ', ' ', ' ', ' ', ' ']

        # Get form data
        contact_name = self.name.get()
        address = self.address.get()
        city = self.city.get()
        mobile = self.mobile.get()
        email = self.email.get()

        field_vars = [contact_name, address, city, mobile, email]

        # Add form data to field_list
        for i in range(5):
            field_list[i] = field_vars[i]

        if field_list[0] != '':
            functions.add_contact(field_list)
        else:
            self.c = cw.confirmationWindow(self.master)

        gui.mainWindow(self.master)
        self.close_window()

    def __init__(self, master):
        top = self.top = tk.Toplevel(master)
        self.master = master
        top.title('Add Contact')

        # name
        self.name_label = tk.Label(top, font='arial 12', text='Name:')
        self.name_label.grid()
        self.name = tk.Entry(top, font='arial 12')
        self.name.grid(row=0, column=1, padx=10)

        # address
        self.address_label = tk.Label(top, font='arial 12', text='Address:')
        self.address_label.grid(row=2)
        self.address = tk.Entry(top, font='arial 12')
        self.address.grid(row=2, column=1)

        # city
        self.city_label = tk.Label(top, font='arial 12', text='City:')
        self.city_label.grid(row=4)
        self.city = tk.Entry(top, font='arial 12')
        self.city.grid(row=4, column=1)

        # mobile phone
        self.mobile_label = tk.Label(top, font='arial 12', text='Mobile Phone:')
        self.mobile_label.grid(row=8)
        self.mobile = tk.Entry(top, font='arial 12')
        self.mobile.grid(row=8, column=1)

        # email
        self.email_label = tk.Label(top, font='arial 12', text='Email:')
        self.email_label.grid(row=9)
        self.email = tk.Entry(top, font='arial 12')
        self.email.grid(row=9, column=1)

        # cancel
        self.cancel_button = tk.Button(top, font='arial 12', bg='red', text='Cancel', command=self.close_window)
        self.cancel_button.grid(row=12, column=1, pady=10)

        # Add
        self.add_button = tk.Button(top, font='arial 12', text='Add', command=self.field_return)
        self.add_button.grid(row=12, column=1, pady=10, padx=10, sticky=tk.E)
