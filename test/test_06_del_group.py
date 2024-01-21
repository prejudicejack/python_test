# -*- coding: utf-8 -*-
from model.group import SelectGroupByName
from model.group import Group


def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.delete_first_group()


def test_delete_group_by_title(app):
    if app.group.group_by_title_count(selected_group="some name") == 0:
        app.group.create(Group(name="some name"))
    app.group.delete_group_by_title(SelectGroupByName(name="some name"))


def test_delete_all_groups(app):
    if app.group.count() <= 1:
        app.group.create(Group(name="test"))
        app.group.create(Group(name="test2"))
    app.group.delete_all_groups()
