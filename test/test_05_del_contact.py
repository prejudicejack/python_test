# -*- coding: utf-8 -*-
from model.contact import SelectContactByName
from model.contact import Contact
from random import randrange


def test_delete_first_contact(app):
    if app.contact.contact_count() == 0:
        app.contact.create(Contact(first_name="name to modify"))
    old_contacts = app.contact.get_contacts_list()
    app.contact.delete_first_contact()
    assert len(old_contacts) - 1 == app.contact.contact_count()
    new_contacts = app.contact.get_contacts_list()
    old_contacts[0:1] = []
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_delete_some_contact(app):
    if app.contact.contact_count() == 0:
        app.contact.create(Contact(first_name="name to modify"))
    old_contacts = app.contact.get_contacts_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    assert len(old_contacts) - 1 == app.contact.contact_count()
    new_contacts = app.contact.get_contacts_list()
    old_contacts[index:index + 1] = []
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_delete_contact_by_name(app):
    if app.contact.contact_by_title_count(first_name="Lucy", lastname="Sunrise") == 0:
        app.contact.create(Contact(first_name="Lucy", lastname="Sunrise"))
    old_contacts = app.contact.get_contacts_list()
    test_contact_index = []
    for i in range(0, len(old_contacts)):
        if old_contacts[i].first_name == 'Lucy' and old_contacts[i].lastname == 'Sunrise':
            test_contact_index.append(i)
            break
    app.contact.delete_contact_by_name(SelectContactByName(first_name="Lucy", lastname="Sunrise"))
    assert len(old_contacts) - 1 == app.contact.contact_count()
    new_contacts = app.contact.get_contacts_list()
    old_contacts[test_contact_index[0]:test_contact_index[0] + 1] = []
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_delete_all_contacts(app):
    if app.contact.contact_count() <= 1:
        app.contact.create(Contact(first_name="name to modify"))
        app.contact.create(Contact(first_name="name to modify new"))
    old_contacts = app.contact.get_contacts_list()
    max_index = len(old_contacts)
    app.contact.delete_all_contacts()
    assert (len(old_contacts) > app.contact.contact_count() == 0)
    new_contacts = app.contact.get_contacts_list()
    old_contacts[0:max_index] = []
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
