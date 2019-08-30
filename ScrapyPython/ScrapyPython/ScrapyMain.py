# File: ScrapyMain.py
# Create: ytouch
# Email : gisdoing@gmail.com
# Version: V1.0.0
# Brief: a basic tool to scrapy website
# ModifyUpdate:
# VersionUpdateInfo:

import os
import sys


class ScrapyTool():
    '''
    @brief:简单的工具整合
    '''
    def __init__(self):
        print('初始化工具')

    def checkTool(self,tooltype):
        '''
        :param tooltype:工具类型，根据Enum来进行选择
        :return: bool :选择成功or失败
        '''
        self.CurTool = tooltype #绑定当前工具，用于后续调用
        return True

    def runTool(self):
        '''
        :return: True:执行成功，False：执行失败
        '''
        return True

