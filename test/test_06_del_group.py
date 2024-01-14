# -*- coding: utf-8 -*-
from model.group import SelectGroupByName


def test_delete_first_group(app):
    app.group.delete_first_group()


def test_delete_group_by_title(app):
    app.group.delete_group_by_title(SelectGroupByName(name="some name"))


def test_delete_all_groups(app):
    app.group.delete_all_groups()
