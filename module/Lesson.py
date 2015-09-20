#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Lesson(object):
    def __init__(self):
        self._path = None
        self._link = None

    def set_path(self, path):
        self._path = path

    def get_path(self):
        return self._path

    def set_link(self, link):
        self._link = link

    def get_link(self):
        return self._link
