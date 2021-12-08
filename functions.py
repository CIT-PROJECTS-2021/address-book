import sys

sys.path.insert(0, 'GUI')

from tkinter import *
import db
import new_book


def select_contact(contact):
    for row in db.get_entry(db.get_id(contact)):
        return row


def add_contact(contact):
    db.insert_contact(contact)


def delete_contact(contact):
    db.delete_contact(db.get_id(contact))


def edit_contact(entry_id, contact):
    db.edit_contact(entry_id, contact)


def search(search_string):
    return db.search_contact(search_string)


if __name__ == "__main__":
    root = Tk()
    root.geometry('800x600')
    root.config(bg='Gray')
    root.title('Address Book')
    new_book.addNewBookWindow(root)
    root.mainloop()
