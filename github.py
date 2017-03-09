import json
import sys
import os
class Github(object):
    #https://github.com/worson/jianshu-programmer/blob/master/assets/JitPackHome.png?raw=true
    """docstring for ."""
    user=""
    prjName=""

    def __init__(self, user="",prjName=""):
        if user=="" or prjName=="":
            data=self._readConfig()
            if data:
                user=data["user"]
                prjName=data["prjName"]
        self.user = user
        self.prjName = prjName
    def format(self,url):
        name=url["url"].split("/")[-1]
        newUrl="https://github.com/%s/%s/blob/master/assets/%s?raw=true" %(self.user,self.prjName,name)
        url["newUrl"]=newUrl
        url['new']="![%s](%s)" %(url["name"],newUrl)
        return url['new']
    def _readConfig(self):
        fileName= "./data/github.cfgd"
        if os.path.exists(fileName) :
            json_input=open(fileName)
            json_str=json_input.read()
            parse_data = json.loads(json_str)
            return parse_data
        else:
            return

if __name__ == "__main__":
    gitHub=Github()
    # gitHub=Github('worson','jianshu')
    print gitHub._readConfig()
    # print gitHub.user,gitHub.prjName
    print gitHub.format({'url': '/assets/balabala.png', 'line': 11, 'name': 'newPicture'})
