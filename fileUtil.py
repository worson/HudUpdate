# -*- coding:utf-8 -*-
import os
import re
def getFolderFiles(path,reg,recursive=False):
    current_files = os.listdir(path)
    all_files = []
    for file_name in current_files:
        full_file_name = os.path.join(path, file_name)
        if recursive and os.path.isdir(full_file_name):
            next_level_files = getFolderFiles(full_file_name,reg,recursive)
            all_files.extend(next_level_files)
        elif re.match(reg , file_name, re.M|re.I):
            all_files.append(full_file_name)

    return all_files

def getUpdateFile(files,outPath):
    return files

def writeFile(filename,content):
    if filename and content:
        dstPath=os.path.dirname(filename)
        if not os.path.exists(dstPath):
            os.makedirs(dstPath)
        with open(filename,'w') as file:
            file.write(content)

def _testWrite():
    writeFile('./data/test.txt','hello ')
def _testFindFile():
    filePath='./';
    outPath=os.path.join(filePath,'out')
    files = getFolderFiles('./','\S+\.md',recursive=True)
    updateFiles=getUpdateFile(files,outPath)

    line = "wang.txt"
    matchObj = re.match( '\S+\.txt', line, re.M|re.I)
    # print matchObj.group()
    # print os.listdir('./')
if __name__ == "__main__":
    _testWrite()
