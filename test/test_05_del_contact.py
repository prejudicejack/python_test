# -*- coding: utf-8 -*-
from model.contact import SelectContactByName
from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.contact_count() == 0:
        app.contact.create(Contact(first_name="name to modify"))
    app.contact.delete_first_contact()


def test_delete_contact_by_name(app):
    if app.contact.contact_by_title_count(first_name="Lucy", lastname="Sunrise") == 0:
        app.contact.create(Contact(first_name="Lucy", lastname="Sunrise"))
    app.contact.delete_contact_by_name(SelectContactByName(first_name="Lucy", lastname="Sunrise"))


def test_delete_all_contacts(app):
    if app.contact.contact_count() <= 1:
        app.contact.create(Contact(first_name="name to modify"))
        app.contact.create(Contact(first_name="name to modify new"))
    app.contact.delete_all_contacts()
