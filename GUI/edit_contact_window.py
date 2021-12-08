import tkinter as tk
import functions
import edit_confirmation_window as editcw
import add_confirmation_window as addcw
import gui


class editContactWindow(object):

    def popup_confirmation(self, field_list, entry_id):
        # Open confirmation window
        self.c = editcw.confirmationWindow(self.master, field_list, entry_id)
        self.master.wait_window(self.c.top)

    def field_return(self):
        # returns data to popup_confirmation()

        # List to hold form data
        field_list = ['', '', '', '', '']

        # Get form data
        name = self.name.get()
        address = self.address.get()
        city = self.city.get()
        mobile = self.mobile.get()
        email = self.email.get()

        field_vars = [name, address, city, mobile, email]

        # Add form data to field_list
        for i in range(5):
            field_list[i] = field_vars[i]

        if field_list[0] != '':
            self.popup_confirmation(field_list, self.entry_id)

        else:
            self.c = addcw.confirmationWindow(self.master)

        gui.mainWindow(self.master).search_query()
        self.close_window()

    def close_window(self):
        self.top.destroy()

    def grab_contact(self):
        # Inserts contact information into fields.
        name_entry = functions.select_contact(self.name_old)

        self.name.insert(0, str(name_entry[0]))
        self.address.insert(0, str(name_entry[1]))
        self.city.insert(0, str(name_entry[2]))
        self.mobile.insert(0, str(name_entry[3]))
        self.email.insert(0, str(name_entry[4]))

    def clear_text_entries(self):
        # Clears any value in text fields.
        self.name.delete(0, tk.END)
        self.address.delete(0, tk.END)
        self.city.delete(0, tk.END)
        self.mobile.delete(0, tk.END)
        self.email.delete(0, tk.END)

    def __init__(self, master, name, entry_id):
        top = self.top = tk.Toplevel(master)
        self.entry_id = entry_id
        self.name_old = name
        self.master = master
        top.title('Edit Contact')

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

        # Save
        self.save_button = tk.Button(top, font='arial 12', bg='blue', text='Save', command=self.field_return)
        self.save_button.grid(row=12, column=1, pady=10, padx=10, sticky=tk.E)

        self.grab_contact()
