#!/usr/bin/env python
# -*- coding: utf-8 -*-
from module.Lesson import Lesson
from module.Video import Video
import os
import json
import requests
import Utils
import Constant


# 抓取某个课程的视频对象列表
def spider_lesson_videos(lesson):
    lesson_videos = []
    req = requests.get(lesson.get_link())
    json_videos = json.loads(req.text)
    index = 0
    for json_video in json_videos["data"]["video_list"]:
        page = None
        if index < 10:
            page = "0" + str(index)
        else:
            page = str(index)

        video = Video()
        video.set_link(json_video["video_url"])

        video.set_name(Utils.filter_file_name(json_video["video_name"]) + Utils.get_file_type(video.get_link()))
        video.set_name(
            page + "_" + Utils.filter_file_name(json_video["video_name"]) + Utils.get_file_type(video.get_link()))
        if not (Utils.file_exist(video.get_path())):
            fd = os.open(video.get_path(), os.O_CREAT)
            video.set_download_status(False)
            os.close(fd)
            # print "--file :" + video.get_path()
        else:
            if os.path.getsize(video.get_path()) > Constant.fie_min_size:
                video.set_download_status(True)
            else:
                video.set_download_status(False)

        lesson_videos.append(video)
        index += 1

    return lesson_videos


# 抓取整个专题的所有视频里列表
def spider_videos_link(url):
    videos = []
    req = requests.get(url)
    json_stages = json.loads(req.text)

    for json_stage in json_stages["data"]["stage"]:
        stage_path = Utils.filter_file_name(Constant.save_path + os.sep + json_stage["stage_name"])
        page = 0
        for json_lesson in json_stage["list"]:
            lesson = Lesson()
            lesson.set_link(Constant.itemLinkPartLink + json_lesson["course_id"])
            lesson.set_path(Utils.filter_file_name(stage_path + os.sep + str(page) + "_" + json_lesson["name"]))
            if not (Utils.file_exist(lesson.get_path())):
                os.makedirs(lesson.get_path())
                # print "dir :" + lesson.get_path()
            lesson_videos = spider_lesson_videos(lesson)
            for item in lesson_videos:
                videos.append(item)
            page += 1

    return videos
