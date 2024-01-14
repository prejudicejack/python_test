# -*- coding: utf-8 -*-
from model.contact import SelectContactByName


def test_delete_first_contact(app):
    app.contact.delete_first_contact()


def test_delete_contact_by_name(app):
    app.contact.delete_contact_by_name(SelectContactByName(first_name="Lucy", lastname="Sunrise"))


def test_delete_all_contacts(app):
    app.contact.delete_all_contacts()
