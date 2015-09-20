#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

# UUID
uuid = "05c703bdd9b140f18c99ffc5e648b85b"

# Client
client = "android"

# UserId
user_id = "49489"

# 文件最小不小于1024个字节,小于1024判断文件不完整,需要重新下载
fie_min_size = 1024

# 文件保存目录
save_path = os.path.pardir + os.sep + "video"

# python专题链接
link = "http://api.maiziedu.com/v2/getCareerDetail?UUID=%s&careerId=13&client=%s&userId=%s" % (uuid,
                                                                                               client,
                                                                                               user_id)

# 课程视频下载链接的link的片段
itemLinkPartLink = "http://api.maiziedu.com/v2/getCoursePlayInfo/?UUID=%s&client=%s&userId=%s&courseId=" % (uuid,
                                                                                                            client,
                                                                                                            user_id)
