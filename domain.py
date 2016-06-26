#coding: utf-8

import os

class Relationships:
    def __init__(self, name, _from, to, on):
        self._name = name
        self._from = _from
        self._to = to
        self._on = on

class Column:
    def __init__(self, name, kind, description):
        self._name = name
        self._kind = kind
        self._description = description

class DataTable:
    def __init__(self, name):
        self._name = name
        self._columns = []
        self._references = []
        self._referenced = []
        self._data = []

    def add_column(self, name, kind, description=""):
        column = Column(name, kind, description=description)
        self._columns.append(column)
        return column

    def add_references(self, name, to, on):
        relationship = Relationships(name, self, to, on)
        self._references.append(relationship)

    def add_referenced(self, name, by, on):
        relationship = Relationships(name, by, self, on)
        self._referenced.append(relationship)

