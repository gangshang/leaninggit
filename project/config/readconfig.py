#-*-coding:utf-8-*-
# author: wangjinqi
# date：2019-06-05
import os
import configparser
import time
'''
cur_path=os.path.dirname(os.path.realpath(__file__))#获取当前文件的绝对路径
print(cur_path)
config_path=os.path.join(cur_path,'config.ini')#获取配置文件的路径
print(config_path)
'''
class ReadConfig():
    '''读取配置文件的类'''
    def __init__(self):
        cur_path = os.path.dirname(os.path.realpath(__file__))  # 获取当前文件的绝对路径
        config_path = os.path.join(cur_path, 'config.ini')  # 获取配置文件的路径
        self.config=configparser.ConfigParser()
        self.config.read(config_path, 'utf-8')#读取配置文件
    '''获取db'''
    def get_db(self,key):
        vaule= self.config.get('db',key)  # 默认获取的类型为字符串
        return vaule
    '''获取数据库备份地址'''
    def get_backuppath(self,key):
        vaule=self.config.get('backuppath',key)
        return vaule
    '''获取json数据地址'''
    def get_json(self,key):
        vaule=self.config.get('json',key)
        return vaule
    '''获取Excel用例存放地址'''
    def get_excel(self,key):
        vaule=self.config.get('excel',key)
        return vaule

if __name__=='__main__':
    a=int(ReadConfig().get_db('port'))
    print(a)
    print(type(a))
    b=ReadConfig().get_backuppath('backuppath')
    print(b)
    backupdate = time.strftime('%Y%m%d')
    print(backupdate)
    c=b+"test"+"-" +backupdate + ".sql"
    print(c)

