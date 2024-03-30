# -*- coding: utf-8 -*-
from model.group import Group
from model.group import SelectGroupByName
import random


def test_modify_first_group(app, db, json_groups, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="to modify", header="to modify 2", footer="to modify 3"))
    old_groups = db.get_group_list()
    group = json_groups
    group.id = old_groups[0].id
    app.group.modify_group_by_id(group.id, group)
    assert len(old_groups) == len(db.get_group_list())
    new_groups = db.get_group_list()
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


def test_modify_some_group(app, db, json_groups, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="to modify", header="to modify 2", footer="to modify 3"))
    old_groups = db.get_group_list()
    group = json_groups
    group.id = random.choice(old_groups).id
    app.group.modify_group_by_id(group.id, group)
    assert len(old_groups) == len(db.get_group_list())
    new_groups = db.get_group_list()
    modified_group_index = []
    for i in range(0, len(old_groups)):
        if old_groups[i].id == group.id:
            modified_group_index.append(i)
    old_groups[modified_group_index[0]] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


def test_edit_group_by_title(app, db, json_groups, check_ui):
    if app.group.group_by_title_count(selected_group="test_group") == 0:
        app.group.create(Group(name="test_group"))
    old_groups = db.get_group_list()
    group = json_groups
    test_group_index = []
    for i in range(0, len(old_groups)):
        if old_groups[i].name == 'test_group':
            test_group_index.append(i)
    group.id = old_groups[test_group_index[0]].id
    app.group.edit_all_fields_in_group_selected_by_title(group, SelectGroupByName(name="test_group"))
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[test_group_index[0]] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

