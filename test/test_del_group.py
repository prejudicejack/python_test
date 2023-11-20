# -*- coding: utf-8 -*-
from model.group import SelectGroupByName


def test_delete_first_group(app):
    app.session.login(user_name="admin", password="secret")
    app.group.delete_first_group()
    app.session.logout()


def test_delete_group_by_title(app):
    app.session.login(user_name="admin", password="secret")
    app.group.delete_group_by_title(SelectGroupByName(name="test_group"))
    app.session.logout()
