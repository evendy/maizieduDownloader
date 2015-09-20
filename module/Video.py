#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json


class Video(object):
    def __init__(self):
        self.path = None
        self.name = None
        self.link = None
        self.d_status = False

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_link(self, link):
        self.link = link

    def get_link(self):
        return self.link

    def set_download_status(self, status):
        self.d_status = status

    def get_download_status(self):
        return self.d_status

    def set_path(self, path):
        self.path = path

    def get_path(self):
        return self.path


class VideoEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Video):
            return {"name": obj.get_name(), "path": obj.get_path(), "link": obj.get_link(),
                    "d_status": obj.get_download_status()}
            return json.JSONEncoder.default(self, obj)
