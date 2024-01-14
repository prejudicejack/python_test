# -*- coding: utf-8 -*-
from model.group import Group
from model.group import SelectGroupByName


def test_edit_first_group(app):
    app.group.edit_all_fields_in_first_group(Group(name="new name", header="new header", footer="new footer"))


def test_edit_group_by_title(app):
    app.group.edit_all_fields_in_group_selected_by_title(Group(name="some name", header="some header", footer="some footer"),
                                                         SelectGroupByName(name="test_group"))


def test_modify_group_name(app):
    app.group.modify_first_group(Group(name="New name 1"))


def test_modify_group_header(app):
    app.group.modify_first_group(Group(header="New header 1"))


def test_modify_group_footer(app):
    app.group.modify_first_group(Group(footer="New footer 1"))
