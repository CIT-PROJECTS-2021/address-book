import sqlite3 as sql
import os.path as path
import config as cfg


def db_init(book_name):
    # Create/Open and initialize a database
    if db_exists(book_name):
        cfg.DB = sql.connect(book_name + '.ab')
        cfg.C = cfg.DB.cursor()
        print('Database already exists')

    else:
        cfg.DB = sql.connect(book_name + '.ab')
        cfg.C = cfg.DB.cursor()
        create_table = '''CREATE TABLE Contacts(Name TEXT, Address TEXT, City TEXT, Mobile TEXT, Email TEXT) '''
        cfg.C.execute(create_table)
        cfg.DB.commit()
        print('Table created')


def db_exists(db_name):
    if path.isfile(db_name + '.ab'):
        return True
    else:
        return False


def get_id(name):
    entry_id = "SELECT rowid, * FROM Contacts WHERE Name = ?"
    cfg.C.execute(entry_id, [name])
    for row in cfg.C:
        return row[0]


def insert_contact(contact):
    cfg.C.execute('INSERT INTO Contacts VALUES (?,?,?,?,?)',
                  contact)
    cfg.DB.commit()


def delete_contact(entry_id):
    cfg.C.execute("DELETE FROM Contacts WHERE rowid = ?", [entry_id])


def get_entry(entry_id):
    cfg.C.execute("SELECT * FROM Contacts WHERE rowid = ?", [entry_id])
    return cfg.C


def db_commit():
    cfg.DB.commit()


def edit_contact(entry_id, entry):
    entry_update = '''UPDATE Contacts SET Name= ?, Address ?, City = ?, Mobile = ?, Email = ?,WHERE rowid = ? '''

    cfg.C.execute(entry_update, [entry[0], entry[1], entry[2], entry[3],
                                 entry[4], '{}'.format(entry_id)])


def search_contact(search_str):
    search_name = '''SELECT * FROM Contacts WHERE (Name|| Address || City || Mobile || Email) LIKE '%' || ? || '%' ORDER BY Name ASC'''
    cfg.C.execute(search_name, [search_str])  

    return cfg.C
