# -- coding: UTF-8

import os
import shutil


# 删除report文件下的log、截图与测试报告
def reports_removed():
    delList = []
    delDir = '/WORK/workspace/python/shanghutong20_API/report/'
    delList = os.listdir(delDir)
    for f in delList:
        filePath = os.path.join(delDir, f)
        if os.path.isfile(filePath):
            os.remove(filePath)
            # print self.filePath + 'was removed!'
        elif os.path.isdir(filePath):
            shutil.rmtree(filePath, True)
            # print "Directory:" + self.filePath + "was removed!"


def results_removed():
    delList = []
    delDir = '/WORK/workspace/python/report/shanghutong20'
    delList = os.listdir(delDir)
    for f in delList:
        filePath = os.path.join(delDir, f)
        if os.path.isfile(filePath):
            os.remove(filePath)
            # print self.filePath + 'was removed!'
        elif os.path.isdir(filePath):
            shutil.rmtree(filePath, True)
            # print "Directory:" + self.filePath + "was removed!"
