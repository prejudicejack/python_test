# -*- coding: utf-8 -*-
import random

from model.contact import Contact
import random


def test_edit_first_contact(app, db, json_contacts):
    if len(db.get_contacts_list()) == 0:
        app.contact.create(Contact(first_name="name to modify"))
    old_contacts = db.get_contacts_list()
    contact = json_contacts
    contact.id = old_contacts[0].id
    app.contact.edit_first_contact(contact)
    assert len(old_contacts) == len(db.get_contacts_list())
    new_contacts = db.get_contacts_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_edit_some_contact(app, db, json_contacts):
    if len(db.get_contacts_list()) == 0:
        app.contact.create(Contact(first_name="name to modify"))
    old_contacts = db.get_contacts_list()
    contact = json_contacts
    contact.id = random.choice(old_contacts).id
    app.contact.edit_contact_by_id(contact.id, contact)
    assert len(old_contacts) == len(db.get_contacts_list())
    new_contacts = db.get_contacts_list()
    modified_contact_index = []
    for i in range(0, len(old_contacts)):
        if old_contacts[i].id == contact.id:
            modified_contact_index.append(i)
    old_contacts[modified_contact_index[0]] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
