# -*- coding: utf-8 -*-
from application import Application
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_create_contact(app):
    app.login(user_name="admin", password="secret")
    app.create_contact(first_name="Lucy",
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
                       selected_group="2",
                       address2="some street next",
                       phone2="12",
                       notes="sun")
    app.logout()
