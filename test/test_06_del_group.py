# -*- coding: utf-8 -*-
from model.group import SelectGroupByName
from model.group import Group
import random


def test_delete_first_group(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    group = old_groups[0]
    app.group.delete_group_by_id(group.id)
    new_groups = db.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups.remove(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_delete_some_group(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.delete_group_by_id(group.id)
    new_groups = db.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups.remove(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_delete_group_by_title(app, db):
    if app.group.group_by_title_count(selected_group="some name") == 0:
        app.group.create(Group(name="some name"))
    old_groups = db.get_group_list()
    test_group_index = []
    for i in range(0, len(old_groups)):
        if old_groups[i].name == 'some name':
            test_group_index.append(i)
            break
    app.group.delete_group_by_title(SelectGroupByName(name="some name"))
    new_groups = db.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups[test_group_index[0]:test_group_index[0]+1] = []
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_delete_all_groups(app, db):
    if len(db.get_group_list()) <= 1:
        app.group.create(Group(name="test"))
        app.group.create(Group(name="test2"))
    old_groups = db.get_group_list()
    max_index = len(old_groups)
    app.group.delete_all_groups()
    new_groups = db.get_group_list()
    assert (len(old_groups) > len(new_groups) == 0)
    old_groups[0:max_index] = []
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
