#!/usr/bin/env python
# -*- coding: utf-8 -*-
from module.Video import *
import spider
import Utils
import downloader
import Constant
import sys

reload(sys)

# Python 设置系统默认编码 window默认系统编码为ascii,容易引起中文乱码
sys.setdefaultencoding('utf8')


def spider_videos():
    videos = spider.spider_videos_link(Constant.link)
    print "spider video's size:" + str(len(videos))
    Utils.write_2_mark(videos)
    print "write_2_mark success"


def async_videos_status():
    Utils.async_download_status()
    need_videos = Utils.get_need_download_videos()
    print "need download video's size:" + str(len(need_videos))


def download_un_download_videos():
    need_videos = Utils.get_need_download_videos()
    print "need download video's size:" + str(len(need_videos))
    downloader.download_videos(need_videos)
    print " download videos  success"


def test():
    videos = []
    for index in range(5):
        video = Video()
        video.set_name("中文." + str(index))
        video.set_download_status(False)
        video.set_path("ddd")
        video.set_link(video.get_name())
        videos.append(video)

    Utils.write_2_mark(videos)
    print "write_2_mark success"

    need_videos = Utils.get_need_download_videos()
    print "need download video's size:" + str(len(need_videos))
    for item in need_videos:
        print item.get_name()


if __name__ == '__main__':
    # spider_videos()
    # async_videos_status()
    # download_un_download_videos()
    stest()
