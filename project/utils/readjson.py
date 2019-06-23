#-*-coding:utf-8-*-
# author: wangjinqi
# date：2019-06-07

import json
from config import readconfig
import os

class ReadJson():

    def __init__(self,name='user.json'):
        self.data=self.read_json(name)

    '''根据文件名读取整个文件'''
    def read_json(self,name):
        rf=readconfig.ReadConfig()
        fp=rf.get_json('json')   #从配置文件中读取json文件存放的地址
        fp1=os.path.join(fp,name)#拼接地址和json文件名
        with open(fp1) as fp2:   #打开文件
            data=json.load(fp2)  #加载json文件
            return data

    '''根据关键字获取对应的json数据'''
    def get_json(self,key):
        return self.data[key]


if __name__=='__main__':
    a=ReadJson('user.json')
    b=a.get_json('user1')
    print(b)