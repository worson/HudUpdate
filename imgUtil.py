# -*- coding:utf-8 -*-
def findImgUrl(line):
    # print line
    if "![" in line:
        imgStartIndex=line.index('![')+2;
        imgEndIndex=line.index('](');
        urlStartIndex=line.index('](')+2;
        urlEndIndex=line.index(')');
        name= line[imgStartIndex:imgEndIndex]
        url=line[urlStartIndex:urlEndIndex]
        old=line[imgStartIndex-2:urlEndIndex+1]
        return name,url,old
    return None

def findFileImgUrl(fileName):
    imgUrl=[]
    with open(fileName) as file:
        lines=file.readlines()
        i=0
        for line in lines:
            url=findImgUrl(line)
            if url!=None:
                # print line
                dict={'line':i,'name':url[0],'url':url[1],"old":url[2]}
                imgUrl.append(dict)#[i,url[0],url[1]]
            i=i+1
    return imgUrl

if __name__ == "__main__":
    url=findImgUrl("ieiieie![桌面图片](wangshengxing)eee")
    print url[0],url[1]
    print findFileImgUrl("/Users/wangshengxing/tool/python/markdown/data/test.md")
    print "0123456789".replace("345","abc")
