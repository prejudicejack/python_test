# -*- coding: utf-8 -*-
from application import Application
import pytest
from group import Group


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.login(user_name="admin", password="secret")
    app.create_group(Group(name="test_group", header="some header", footer="some footer"))
    # app.create_group(group_name="test_group", group_header="some header", group_footer="some footer")
    app.logout()


def test_add_empty_group(app):
    app.login(user_name="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()
