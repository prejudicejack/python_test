# -*- coding: utf-8 -*-
from model.contact import Contact


def test_create_contact_full(app):
    old_contacts = app.contact.get_contacts_list()
    contact = Contact(first_name="Lucy", middlename="Michelle", lastname="Sunrise", nickname="Lu", title="Title1",
                      company="Company", address="street Company", home_phone="9998999", mobile_phone="7654",
                      work_phone="123234", fax="567456", email1="some@mail.com", email2="next@mail.com",
                      email3="onemore@mail.com", homepage="https://somepage.com", birthday_day="30",
                      birthday_month="October", birthday_year="1978", anniversary_day="10",
                      anniversary_month="November",
                      anniversary_year="2000", address2="some street next", phone2="12", notes="sun")
    app.contact.create(contact)
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_create_contact_half_filled(app):
    old_contacts = app.contact.get_contacts_list()
    contact = Contact(first_name="Elsa", middlename="Michelle", lastname="Sunrise", nickname="El", work_phone="123234",
                      email1="some@mail.com", birthday_day="10", birthday_month="June", birthday_year="1987",
                      anniversary_day="3", anniversary_month="August", anniversary_year="2010")
    app.contact.create(contact)
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_create_contact_empty_name(app):
    old_contacts = app.contact.get_contacts_list()
    contact = Contact(first_name="", middlename="", lastname="")
    app.contact.create(contact)
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
