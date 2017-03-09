import os
github="github"
user="user"
prjName="prjName"

_workdir="./"
config={github:{user:'usr',prjName:"prjName"}}



def getConfig():
    global config
    return config

def setWorkPath(path):
    global _workdir
    _workdir=path

def configFilePath():
    global _workdir
    return os.path.join(_workdir,'config/usr.config')

if __name__ == '__main__':
    setWorkPath('hhh')
    print configFilePath()
    print getConfig().keys()
