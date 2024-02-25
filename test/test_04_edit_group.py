# -*- coding: utf-8 -*-
from model.group import Group
from model.group import SelectGroupByName
from random import randrange


def test_modify_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="to modify", header="to modify 2", footer="to modify 3"))
    old_groups = app.group.get_group_list()
    group = Group(name="new name", header="new header", footer="new footer")
    group.id = old_groups[0].id
    app.group.modify_first_group(group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_modify_some_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="to modify", header="to modify 2", footer="to modify 3"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="new name", header="new header", footer="new footer")
    group.id = old_groups[index].id
    app.group.modify_group_by_index(index, group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


# def test_edit_group_by_title(app):
#     if app.group.group_by_title_count(selected_group="test_group") == 0:
#         app.group.create(Group(name="test_group"))
#     old_groups = app.group.get_group_list()
#     group = Group(name="some name", header="some header", footer="some footer")
#     group.id = old_groups[0].id
#     app.group.edit_all_fields_in_group_selected_by_title(group, SelectGroupByName(name="test_group"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)
#     old_groups[0] = group
#     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="to modify"))
    old_groups = app.group.get_group_list()
    group = Group(name="New name 1")
    group.id = old_groups[0].id
    app.group.modify_first_group(group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="to modify"))
    old_groups = app.group.get_group_list()
    group = Group(header="New header 1")
    group.id = old_groups[0].id
    app.group.modify_first_group(group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_modify_group_footer(app):
    if app.group.count() == 0:
        app.group.create(Group(name="to modify"))
    old_groups = app.group.get_group_list()
    group = Group(footer="New footer 1")
    group.id = old_groups[0].id
    app.group.modify_first_group(group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
