#!/usr/bin/env python
# -*- coding: utf-8 -*-
from module.Video import *
import re
import os
import json
import Constant

mark_file = Constant.save_path + os.sep + "mark.txt"


# 获取文件的格式
def get_file_type(file_name):
    re_str = "(\.\w+).*?"
    return re.findall(re_str, file_name, re.S)[-1]


# 过滤文件名中的空格和冒号
def filter_file_name(file_name):
    return file_name.replace(" ", "").replace(u"：", "_")


# 判断文件是否存在
def file_exist(file_name):
    return os.path.exists(file_name)


# 将视频的下载状态写入到mark文件
def write_2_mark(all_videos):
    if file_exist(mark_file):
        os.remove(mark_file)
    os.open(mark_file, os.O_CREAT)
    fd = os.open(mark_file, os.O_RDWR)
    content = json.dumps(all_videos, cls=VideoEncoder, ensure_ascii=False)
    os.write(fd, content)
    os.close(fd)


# 获取所有视频对象列表
def get_need_download_videos():
    videos = []
    fd = os.open(mark_file, os.O_RDONLY)
    content = os.read(fd, 1024*1024)
    json_videos = json.loads(content, encoding="utf-8")
    for json_video in json_videos:
        video = Video()
        video.set_path(json_video["path"])
        video.set_name(json_video["name"])
        video.set_link(json_video["link"])
        video.set_download_status(json_video["d_status"])
        if not video.get_download_status():
            videos.append(video)
    os.close(fd)
    return videos


def async_download_status():
    videos = []
    fd = os.open(mark_file, os.O_RDWR)
    content = os.read(fd, 1024*1024)
    json_videos = json.loads(content, encoding="utf-8")
    for json_video in json_videos:
        video = Video()
        video.set_path(json_video["path"])
        video.set_name(json_video["name"])
        video.set_link(json_video["link"])
        flag = False
        if file_exist(video.get_path()) and os.path.getsize(video.get_path()) > Constant.fie_min_size:
            flag = True
        video.set_download_status(flag)
        videos.append(video)
    os.close(fd)
    write_2_mark(videos)
