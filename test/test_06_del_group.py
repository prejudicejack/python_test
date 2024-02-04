# -*- coding: utf-8 -*-
from model.group import SelectGroupByName
from model.group import Group


def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    app.group.delete_first_group()
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups[0:1] = []
    assert old_groups == new_groups


def test_delete_group_by_title(app):
    if app.group.group_by_title_count(selected_group="some name") == 0:
        app.group.create(Group(name="some name"))
    old_groups = app.group.get_group_list()
    app.group.delete_group_by_title(SelectGroupByName(name="some name"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)


def test_delete_all_groups(app):
    if app.group.count() <= 1:
        app.group.create(Group(name="test"))
        app.group.create(Group(name="test2"))
    old_groups = app.group.get_group_list()
    app.group.delete_all_groups()
    new_groups = app.group.get_group_list()
    assert (len(old_groups) > len(new_groups) == 0)
