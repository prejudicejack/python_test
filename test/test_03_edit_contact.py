# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange


def test_edit_first_contact(app):
    if app.contact.contact_count() == 0:
        app.contact.create(Contact(first_name="name to modify"))
    old_contacts = app.contact.get_contacts_list()
    contact = Contact(first_name="Ann", middlename="Rose", lastname="Maryland", nickname="A", title="Title255",
                      company="Company_ 255", address="255 Company", home_phone="12345678", mobile_phone="8888",
                      work_phone="098765", fax="567866", email1="255@mail.com", email2="next255@mail.com",
                      email3="onemore255@mail.com", homepage="https://somepage255.com", birthday_day="10",
                      birthday_month="July", birthday_year="1995", anniversary_day="3", anniversary_month="March",
                      anniversary_year="2007", address2="some street next 255", phone2="546464345", notes="self")
    contact.id = old_contacts[0].id
    app.contact.edit_first_contact(contact)
    assert len(old_contacts) == app.contact.contact_count()
    new_contacts = app.contact.get_contacts_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_edit_some_contact(app):
    if app.contact.contact_count() == 0:
        app.contact.create(Contact(first_name="name to modify"))
    old_contacts = app.contact.get_contacts_list()
    index = randrange(len(old_contacts))
    contact = Contact(first_name="Mary", middlename="Lin", lastname="Gray", nickname="MM", title="Title255",
                      company="Company_ 255", address="255 Company", home_phone="12345678", mobile_phone="8888",
                      work_phone="098765", email1="255@mail.com")
    contact.id = old_contacts[index].id
    app.contact.edit_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.contact_count()
    new_contacts = app.contact.get_contacts_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
