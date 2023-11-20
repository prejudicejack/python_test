# -*- coding: utf-8 -*-
from model.contact import Contact


def test_create_contact(app):
    app.session.login(user_name="admin", password="secret")
    app.contact.create(Contact(first_name="Lucy",
                               middlename="Michelle",
                               lastname="Sunrise",
                               nickname="Lu",
                               title="Title1",
                               company="Company",
                               address="street Company",
                               home_phone="9998999",
                               mobile_phone="7654",
                               work_phone="123234",
                               fax="567456",
                               email1="some@mail.com",
                               email2="next@mail.com",
                               email3="onemore@mail.com",
                               homepage="https://somepage.com",
                               birthday_day="30",
                               birthday_month="October",
                               birthday_year="1978",
                               anniversary_day="10",
                               anniversary_month="November",
                               anniversary_year="2000",
                               selected_group="test_group",
                               address2="some street next",
                               phone2="12",
                               notes="sun"))
    app.session.logout()
