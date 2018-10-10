# -*- coding:utf-8 -*-
import json,urllib2
import commands
import sys
from optparse import OptionParser

#Add command option
def addParser():
    parser = OptionParser()
    
    parser.add_option("-r", "--robot",
                      help="The robot url of notify. Such as https://oapi.dingtalk.com/robot/send?access_token=4dsadafetregrgtrgsbd0600e3f.",
                      metavar="robot")
                      
    parser.add_option("-t", "--type",
                      help="Notify type. Valid values are:success,fail. Default is success.",
                      metavar="type")

    parser.add_option("-s", "--subject",
                      help="The subject of notify. Default is 持续集成成功.",
                      metavar="subject")

    parser.add_option("-m", "--message",
                  help="The messgae of notify. Default is git commit message.",
                  metavar="message")
                  
    parser.add_option("-p", "--picUrl",
                      help="The picture url of notify. Default is http://img5.imgtn.bdimg.com/it/u=1177344293,1498176672&fm=26&gp=0.jpg",
                      metavar="picUrl")
       
    parser.add_option("-l", "--link",
                      help="The download link of notify. Default is link https://www.baidu.com",
                      metavar="link")

    (options, args) = parser.parse_args()
                      
    return options

def getCommitMessage():
    (status, output) = commands.getstatusoutput('git log --format=%B -n 1')
    return output

def getTextmod(options):
    if options.type=="fail":
        message = options.message
        if message==None:
            message = ""
        message = "!!!持续集成失败:\n"+getCommitMessage() + message
        textmod={"msgtype": "text","text":{"content":message},"at":{"isAtAll": True}}
        textmod = json.dumps(textmod)
        return textmod
    else:
        subject = options.subject
        if subject==None:
           subject = "持续集成成功"

        picUrl = options.picUrl
        if picUrl==None:
           picUrl = "http://img5.imgtn.bdimg.com/it/u=1177344293,1498176672&fm=26&gp=0.jpg"

        link = options.link
        if link==None:
            link = "https://www.baidu.com/"

        message = options.message
        if message==None:
           message = ""
        message = getCommitMessage() + message

        textmod={"msgtype": "link","link":{"title": subject, "text": message, "picUrl": picUrl, "messageUrl": link},"at":{"isAtAll": True}}
        textmod = json.dumps(textmod)
        return textmod

def main():
    reload(sys)
    sys.setdefaultencoding( "utf-8" )
    
    options = addParser()
    
    textmod = getTextmod(options)
    print(textmod)
    header_dict = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',"Content-Type": "application/json"}
    
    url = options.robot
    if url==None:
       return
    req = urllib2.Request(url=url,data=textmod,headers=header_dict)
    res = urllib2.urlopen(req)
    res = res.read()
    print(res)

main()
