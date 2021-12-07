import sys
import tkinter as tk

import add_contact_window as acw
import no_selection as ns
import delete_confirmation_window as dcw
import edit_contact_window as ecw
import functions

sys.path.insert(0, '..')


class mainWindow(object):

    def delete_contact(self, name):
        # Deletes selected contact.
        functions.delete_contact(name)

    def popup_add(self):
        self.w = acw.newContactWindow(self.master)
        self.master.wait_window(self.w.top)

    def no_edit(self):
        # Text Fields on main window readonly.
        self.name.configure(state='readonly')
        self.address.configure(state='readonly')
        self.city.configure(state='readonly')
        self.mobile.configure(state='readonly')
        self.email.configure(state='readonly')

    def on_select(self, event):
        w = event.widget
        name = str(self.address_list.get(self.address_list.curselection()))
        self.clear_entries()

        name_entry = functions.select_contact(name)

        self.name.insert(0, str(name_entry[0]))
        self.address.insert(0, str(name_entry[1]))
        self.city.insert(0, str(name_entry[2]))
        self.mobile.insert(0, str(name_entry[3]))
        self.email.insert(0, str(name_entry[4]))

        # User cannot edit entries on main GUI,before clicking button.
        self.name.configure(state='readonly')
        self.address.configure(state='readonly')
        self.city.configure(state='readonly')
        self.mobile.configure(state='readonly')
        self.email.configure(state='readonly')

    def clear_entries(self):
        self.name.configure(state='normal')
        self.address.configure(state='normal')
        self.city.configure(state='normal')
        self.mobile.configure(state='normal')
        self.email.configure(state='normal')

        self.name.delete(0, tk.END)
        self.address.delete(0, tk.END)
        self.city.delete(0, tk.END)
        self.mobile.delete(0, tk.END)
        self.email.delete(0, tk.END)

    def popup_edit(self):
        # Open Edit Contact Window
        try:
            name = str(self.address_list.get(self.address_list.curselection()))
            entry = []

            try:
                entry.append(name.split()[0])
            except:
                entry.append('')

            try:
                entry.append(name.split()[1])
            except:
                entry.append('')

            entry_id = functions.get_id(entry)
            self.k = ecw.editContactWindow(self.master, name, entry_id)
            self.master.wait_window(self.k.top)
        except:
            self.c = ns.confirmationWindow(self.master)

    def popup_confirmation(self):
        try:
            name = str(self.address_list.get(self.address_list.curselection()))
            self.c = dcw.confirmationWindow(self.master, name)
            self.master.wait_window(self.c.top)
        except:
            self.c = ns.confirmationWindow(self.master)

    def __init__(self, master):
        self.master = master
        master.title('Address Book')

        # Scroll bar and box list of contacts
        self.scrollbar = tk.Scrollbar(master)

        # Contact list
        self.address_list = tk.Listbox(master, yscrollcommand=self.scrollbar.set,
                                       height=20)
        self.address_list.grid(row=2, column=10, rowspan=15, padx=15)
        self.scrollbar.config(command=self.address_list.yview)
        self.address_list.bind('<<ListboxSelect>>', self.on_select)

        # Add contact button
        self.add_button = tk.Button(master, font='arial 12', text='Add',
                                    command=self.popup_add)
        self.add_button.grid(row=0, column=0, sticky=tk.W, padx=12)

        # Delete contact button
        self.delete_button = tk.Button(master, font='arial 12', bg='red', text='Delete',
                                       command=self.popup_confirmation)
        self.delete_button.grid(row=11, column=3)

        # Edit contact button
        self.edit_button = tk.Button(master, font='arial 12', bg='blue', text='Edit',
                                     command=self.popup_edit)
        self.edit_button.grid(row=11, column=4, padx=10, sticky=tk.E)

        # The fields to display contact information
        # First name
        self.name_label = tk.Label(master, font='arial 12', text='Name:')
        self.name_label.grid(row=2, column=1)
        self.name = tk.Entry(master, font='arial 12')
        self.name.grid(row=2, column=3)

        # Address
        self.address_label = tk.Label(master, font='arial 12', text='Address:')
        self.address_label.grid(row=3, column=1)
        self.address = tk.Entry(master, font='arial 12')
        self.address.grid(row=3, column=3)

        # City
        self.city_label = tk.Label(master, font='arial 12', text='City:')
        self.city_label.grid(row=4, column=1)
        self.city = tk.Entry(master, font='arial 12')
        self.city.grid(row=4, column=3)

        # Mobile phone
        self.mobile_label = tk.Label(master, font='arial 12', text='Mobile:')
        self.mobile_label.grid(row=5, column=1)
        self.mobile = tk.Entry(master, font='arial 12')
        self.mobile.grid(row=5, column=3)

        # Email
        self.email_label = tk.Label(master, font='arial 12', text='Email:')
        self.email_label.grid(row=6, column=1)
        self.email = tk.Entry(master, font='arial 12')
        self.email.grid(row=6, column=3)

        self.no_edit()  # Make fields readonly
