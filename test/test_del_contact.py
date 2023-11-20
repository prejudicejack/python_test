# -*- coding: utf-8 -*-
from model.contact import SelectContactByName


def test_delete_first_contact(app):
    app.session.login(user_name="admin", password="secret")
    app.contact.delete_first_contact()
    app.session.logout()


def test_delete_contact_by_name(app):
    app.session.login(user_name="admin", password="secret")
    app.contact.delete_contact_by_name(SelectContactByName(first_name="Lucy", lastname="Sunrise"))
    app.session.logout()


def test_delete_all_contacts(app):
    app.session.login(user_name="admin", password="secret")
    app.contact.delete_all_contacts()
    app.session.logout()
