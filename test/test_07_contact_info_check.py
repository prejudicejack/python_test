import re
from model.contact import Contact
from random import randrange


def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contacts_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_phones_from_homepage == merge_phones_like_on_home_page(contact_from_edit_page)


def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contacts_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.home_phone == contact_from_edit_page.home_phone
    assert contact_from_view_page.work_phone == contact_from_edit_page.work_phone
    assert contact_from_view_page.mobile_phone == contact_from_edit_page.mobile_phone
    assert contact_from_view_page.phone2 == contact_from_edit_page.phone2


def test_contact_info_check(app, db):
    contact_from_db = sorted(db.get_contacts_list_like_on_home_page(), key=Contact.id_or_max)
    contact_from_home_page = sorted(app.contact.get_contacts_list(), key=Contact.id_or_max)
    for i in range(len(contact_from_db)):
        assert contact_from_home_page[i].first_name == contact_from_db[i].first_name
        assert contact_from_home_page[i].lastname == contact_from_db[i].lastname
        assert contact_from_home_page[i].address.replace(' ', '') == contact_from_db[i].address.replace(' ', '')
        assert contact_from_home_page[i].all_phones_from_homepage == merge_phones_like_on_home_page(contact_from_db[i])
        assert contact_from_home_page[i].all_emails_from_homepage == merge_emails_like_on_home_page(contact_from_db[i])


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home_phone, contact.mobile_phone, contact.work_phone, contact.phone2]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.email1, contact.email2, contact.email3]))))
