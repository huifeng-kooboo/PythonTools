# File: EnumTools.py
# Create: ytouch
# Email : gisdoing@gmail.com
# Version: V1.0.0
# Brief: some func to do
# ModifyUpdate:
# VersionUpdateInfo:

from enum import Enum

class ToolType(Enum):
    '''
    @brief:已实现的工具类
    '''
    YOUTUBEVIDEO = 1   #爬取YOUTUBE视频
    IQIYIVIDEO = 2     #爬取爱奇艺视频
    TENCENTVIDEO = 3   #爬取腾讯视频
    YOUKUVIDEO = 4     #爬取优酷视频
    DOUBANINFO = 5     #爬取豆瓣信息
    CSDNBLOG = 6       #爬取CSDN博客
    TICKETPLANE = 7    #爬取火车票信息

