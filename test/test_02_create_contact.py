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
                               address2="some street next",
                               phone2="12",
                               notes="sun"))
    app.session.logout()


def test_create_contact2(app):
    app.session.login(user_name="admin", password="secret")
    app.contact.create(Contact(first_name="Elsa",
                               middlename="Michelle",
                               lastname="Sunrise",
                               nickname="El",
                               title="",
                               company="",
                               address="",
                               home_phone="",
                               mobile_phone="",
                               work_phone="123234",
                               fax="",
                               email1="some@mail.com",
                               email2="",
                               email3="",
                               homepage="",
                               birthday_day="10",
                               birthday_month="June",
                               birthday_year="1987",
                               anniversary_day="3",
                               anniversary_month="August",
                               anniversary_year="2010",
                               address2="",
                               phone2="",
                               notes=""))
    app.session.logout()


def test_create_contact3(app):
    app.session.login(user_name="admin", password="secret")
    app.contact.create(Contact(first_name="Test",
                               middlename="MTest",
                               lastname="Test",
                               nickname="Test",
                               title="",
                               company="",
                               address="",
                               home_phone="",
                               mobile_phone="",
                               work_phone="",
                               fax="",
                               email1="",
                               email2="",
                               email3="",
                               homepage="",
                               birthday_day="-",
                               birthday_month="-",
                               birthday_year="",
                               anniversary_day="-",
                               anniversary_month="-",
                               anniversary_year="",
                               address2="",
                               phone2="",
                               notes=""))
    app.session.logout()
