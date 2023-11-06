# -*- coding: utf-8 -*-
from model.group import Group
from conftest import app


def test_add_group(app):
    app.session.login(user_name="admin", password="secret")
    app.group.create(Group(name="test_group", header="some header", footer="some footer"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(user_name="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()
