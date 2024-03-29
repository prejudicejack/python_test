# -*- coding: utf-8 -*-
from model.group import SelectGroupByName
from model.group import Group
from random import randrange


def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    app.group.delete_first_group()
    assert len(old_groups) - 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[0:1] = []
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_delete_some_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    app.group.delete_group_by_index(index)
    assert len(old_groups) - 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index:index+1] = []
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_delete_group_by_title(app):
    if app.group.group_by_title_count(selected_group="some name") == 0:
        app.group.create(Group(name="some name"))
    old_groups = app.group.get_group_list()
    test_group_index = []
    for i in range(0, len(old_groups)):
        if old_groups[i].name == 'some name':
            test_group_index.append(i)
            break
    app.group.delete_group_by_title(SelectGroupByName(name="some name"))
    assert len(old_groups) - 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[test_group_index[0]:test_group_index[0]+1] = []
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_delete_all_groups(app):
    if app.group.count() <= 1:
        app.group.create(Group(name="test"))
        app.group.create(Group(name="test2"))
    old_groups = app.group.get_group_list()
    max_index = len(old_groups)
    app.group.delete_all_groups()
    assert (len(old_groups) > app.group.count() == 0)
    new_groups = app.group.get_group_list()
    old_groups[0:max_index] = []
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
