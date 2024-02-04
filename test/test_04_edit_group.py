# -*- coding: utf-8 -*-
from model.group import Group
from model.group import SelectGroupByName


def test_edit_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="to modify", header="to modify 2", footer="to modify 3"))
    old_groups = app.group.get_group_list()
    app.group.edit_all_fields_in_first_group(Group(name="new name", header="new header", footer="new footer"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_edit_group_by_title(app):
    if app.group.group_by_title_count(selected_group="test_group") == 0:
        app.group.create(Group(name="test_group"))
    old_groups = app.group.get_group_list()
    app.group.edit_all_fields_in_group_selected_by_title(Group(name="some name", header="some header", footer="some footer"),
                                                         SelectGroupByName(name="test_group"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="to modify"))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(name="New name 1"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="to modify"))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(header="New header 1"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_modify_group_footer(app):
    if app.group.count() == 0:
        app.group.create(Group(name="to modify"))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(footer="New footer 1"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
