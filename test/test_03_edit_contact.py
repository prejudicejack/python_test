# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_first_contact(app):
    if app.contact.contact_count() == 0:
        app.contact.create(Contact(first_name="name to modify"))
    app.contact.edit_first_contact(Contact(first_name="Ann",
                                           middlename="Rose",
                                           lastname="Maryland",
                                           nickname="A",
                                           title="Title255",
                                           company="Company_ 255",
                                           address="255 Company",
                                           home_phone="12345678",
                                           mobile_phone="8888",
                                           work_phone="098765",
                                           fax="567866",
                                           email1="255@mail.com",
                                           email2="next255@mail.com",
                                           email3="onemore255@mail.com",
                                           homepage="https://somepage255.com",
                                           birthday_day="10",
                                           birthday_month="July",
                                           birthday_year="1995",
                                           anniversary_day="3",
                                           anniversary_month="March",
                                           anniversary_year="2007",
                                           address2="some street next 255",
                                           phone2="546464345",
                                           notes="self"))

