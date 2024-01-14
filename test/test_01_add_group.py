# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.group.create(Group(name="test_group", header="some header", footer="some footer"))


def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))


def test_add_group_with_filled_header(app):
    app.group.create(Group(name="", header="new header here", footer=""))
