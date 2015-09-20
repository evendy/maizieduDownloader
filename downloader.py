#!/usr/bin/env python
# -*- coding: utf-8 -*-
from multiprocessing.dummy import Pool as ThreadPool
import requests


# 下载所有的视频
def download_videos(videos):
    pool = ThreadPool(4)
    pool.map(download_video, videos)
    pool.close()
    pool.join()


# 下载具体某个视频
def download_video(video):
    print "start download :" + video.get_name()
    try:
        f = open(video.get_path(), "wb")
        req = requests.get(video.get_link())
        f.write(req.content)
        f.flush()
        f.close()
        print "---------- download success :" + video.get_name()
    except (requests.exceptions.ConnectionError, requests.exceptions.HTTPError):
        print "---------- download error :" + video.get_name()
