# -*- coding:utf-8 -*-
import os
from optparse import OptionParser
import subprocess
import logging
import commands
from optparse import OptionParser

log = logging.getLogger("Core.Analysis.Processing")

INTERPRETER = "/usr/bin/python"

class selfException(BaseException):
    def __init__(self,mesg="raise a selfException"):
        print mesg

def raise_exception():
    raise selfException("upload failed!")
    return

#Add command option
def addParser():
    parser = OptionParser()
    
    parser.add_option("-p", "--path",
                      help="uploaded file path. default is ../CIDemo.ipa",
                      metavar="path")
        
    (options, args) = parser.parse_args()
                      
    return options

# 判断字符串是否为空
def isNone(para):
    if para == None or len(para) == 0:
        return True
    else:
        return False

# 上传到fir.im
def uploadToFir(output,changelog):
    httpAddress = None
    if os.path.exists(output):
        print "开始上传" + output
        ret = os.popen("/usr/local/bin/fir publish '%s' --changelog='%s'" % (output,changelog))
        for info in ret.readlines():
            if "Published succeed" in info:
                httpAddress = info
                print httpAddress
                break
    else:
        print "没有找到ipa文件"
    return httpAddress

#获取Git提交信息
def getCommitMessage():
    (status, output) = commands.getstatusoutput('git log --format=%B -n 1')
    return output

# 主函数
def main():
    options = addParser()
    path = options.path
    
    if path==None:
        path = "../CIDemo.ipa"
    
    message = getCommitMessage()
    httpAddress = uploadToFir(path,message)
    
    if not isNone(httpAddress):
        print "upload success:"+httpAddress
    else:
        raise_exception()
    return

main()

