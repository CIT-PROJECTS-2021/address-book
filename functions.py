import sys

sys.path.insert(0, 'GUI')

from tkinter import *
import db
import new_book


def select_contact(contact):
    entry = []

    try:
        if contact.split()[1]:
            entry.append(contact.split()[0])
            entry.append(contact.split()[1])
    except:
        entry.append('')
        entry.append(contact.split()[0])

    for row in db.get_entry(db.get_id(entry)):
        return row


def add_contact(contact):
    db.insert_contact(contact)


def delete_contact(contact):
    entry = []
    try:
        entry.append(contact.split()[0])
    except:
        entry.append('')

    try:
        entry.append(contact.split()[1])
    except:
        entry.append('')

    db.delete_contact(db.get_id(entry))


def edit_contact(entry_id, contact):
    db.edit_contact(entry_id, contact)


def search(search_string):
    return db.search_contact(search_string)


if __name__ == "__main__":
    root = Tk()
    root.geometry('600x400')
    root.config(bg='Gray')
    root.title('Address Book')
    new_book.addNewBookWindow(root)
    root.mainloop()
