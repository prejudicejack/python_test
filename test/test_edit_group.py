# -*- coding: utf-8 -*-
from model.group import Group
from model.group import SelectGroupByName


def test_edit_first_group(app):
    app.session.login(user_name="admin", password="secret")
    app.group.edit_first_group(Group(name="new name", header="new header", footer="new footer"))
    app.session.logout()


def test_edit_group_by_title(app):
    app.session.login(user_name="admin", password="secret")
    app.group.edit_group_by_title(Group(name="some name", header="some header", footer="some footer"),
                                  SelectGroupByName(name="123"))
    app.session.logout()
