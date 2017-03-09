# -*- coding:utf-8 -*-
from github import Github
import imgUtil
import fileUtil as fu
import os
import sys
import shutil
import config as cf
import json
'''
版本：python 2.7
功能：将本地的gitbook格式的所有文件的图片资源引用,全部在另外一个目录生成一个基于github的url格式的的文件
使用: python markdownPhaser.py srcPath dstPath
配置:
    github: user prjName
'''

'''
获取一个文件所有的新url
'''
def parseMarkdown(fullName,format=None):
    # print fullName
    urls=imgUtil.findFileImgUrl(fullName)
    newUrls=[]
    for url in urls:
        format.format(url)
        newUrls.append(url)
    return newUrls

'''
将新的url写入到指定的文件
'''
def writeMarkdown(fullName,dstName,newUrls):
    if fullName and dstName:
        dstPath=os.path.dirname(dstName)
        if not os.path.exists(dstPath):
            print 'mkdir '
            os.makedirs(dstPath)
        if not newUrls:
            shutil.copyfile(fullName,dstName)
            return True
        with open(fullName) as infile,open(dstName,mode='w') as outFile :
            lines=infile.readlines()
            lineIndex=0
            urlIndex=0
            for line in lines:
                if urlIndex < len(newUrls) :
                    url=newUrls[urlIndex]
                    if lineIndex== url["line"]:
                        urlIndex=urlIndex+1
                        print line
                        newLine=line.replace(url["old"],url["new"])
                        print newLine
                        outFile.write(newLine)
                    else:
                        outFile.write(line)
                else:
                    outFile.write(line)
                lineIndex=lineIndex+1
        return True
'''
转换指定的markdown文件
'''
def buildNewMarkdownFile(srcFile,dstFile,parser):
    newUrls=parseMarkdown(srcFile,parser)
    return writeMarkdown(srcFile,dstFile,newUrls)

def buildNewMarkdownFolder(srcPath,outPath,parser,recursive=False):
    files = fu.getFolderFiles(srcPath,'\S+\.md',recursive)
    updateFiles=fu.getUpdateFile(files,outPath)
    # print updateFiles
    for updateFile in updateFiles:
        baseName=os.path.basename(updateFile)
        newFile=os.path.join(outPath,baseName)
        # print newFile
        buildNewMarkdownFile(updateFile,newFile,parser)
def _test_build_folder():
    src="/Users/wangshengxing/tool/python/markdown/data/"
    dst="/Users/wangshengxing/tool/python/markdown/out/"
    parser=Github('worson','jianshu')
    print buildNewMarkdownFolder(src,dst,parser,True)

if __name__ == "__main__":
    print 'main start ...'
    curDir= os.path.dirname(sys.argv[0])
    cf.setWorkPath(curDir)
    configPath=cf.configFilePath()
    config=cf.getConfig()
    if not os.path.exists(configPath) and config.has_key(cf.github):
        # x = input("x: ")
        usr=raw_input('please input your github user name ...\n:')
        prjName=raw_input('please input your github project name ...\n:')
        config[cf.github]={cf.user:usr,cf.prjName:prjName}
        print 'your input : %s %s ' %(usr,prjName)
        content=json.dumps(config)
        fu.writeFile(configPath,content)
    if len(sys.argv)>2:
        src=sys.argv[1]
        dst=sys.argv[1]
        parser=Github('worson','jianshu-programmer')
        # buildNewMarkdownFolder(src,dst,parser,True)
    else:
        print 'please input argv: ...srcPath dstPath...'
    print 'main end !!!'
