import pymysql
import os
import time
from config import readconfig

rf=readconfig.ReadConfig()#实例获取配置文件的类
class MysqlHelper():
    def __init__(self,host=rf.get_db('host'),port=int(rf.get_db('port')),user=rf.get_db('user'),passwd=rf.get_db('passwd'),db=rf.get_db('db'),charset='utf8mb4'):
        self.host=host
        self.port=port
        self.user=user
        self.passwd=passwd
        self.db=db
        self.charset=charset
        #self.backuppath = "D:\python\est1\data\data"  # 定义备份文件夹
        self.backuppath=rf.get_backuppath('backuppath')#读取配置文件里的备份地址
        # backupdate=time.strftime('%Y%m%d_%H%M%S')#获取当前时间并转为字符串格式，定义备份日期
        self.backupdate = time.strftime('%Y%m%d')  # 获取当前时间并转为字符串格式，定义备份日期

    '''连接数据库，获取游标'''
    def open(self):
        self.conn=pymysql.connect(host=self.host,port=self.port,user=self.user,passwd=self.passwd,db=self.db,charset=self.charset)
        self.cursor=self.conn.cursor(cursor=pymysql.cursors.DictCursor)#返回结果以字典显示
        #self.cursor =self.conn.cursor()

    '''释放游标，关闭数据库'''
    def close(self):
        self.cursor.close()
        self.conn.close()

    '''查询数据'''
    def select(self,sql,params):
        try:
            self.open()
            self.cursor.execute(sql,params)#执行sql
            result=self.cursor.fetchall()#获取全部查询结果
            self.close()
            return result
        except Exception as e:
            print(e.message)

    '''增删改数据'''
    def cud(self,sql,params):
        try:
            self.open()
            self.cursor.execute(sql,params)
            effect=self.cursor.rowcount#获取影响行数
            self.conn.commit()
            self.close()
            return effect
        except Exception as e:
            print(e.message)
            self.conn.rollback()

    '''备份数据库'''
    def backup(self):
        try:
            # backupdate=time.strftime('%Y%m%d_%H%M%S')#获取当前时间并转为字符串格式，定义备份日期
            #backupdate = time.strftime('%Y%m%d')  # 获取当前时间并转为字符串格式，定义备份日期
            dumpcmd = "mysqldump -h" + self.host +" "+ "-u" + self.user + " -p" + self.passwd + " " + self.db + " > " + self.backuppath +self.db+ "-" + self.backupdate + ".sql"
            os.system(dumpcmd)
            print('备份成功')
        except Exception as e:
            print(e.message)
    '''还原数据库'''
    def restore(self):
        try:
            loadcmd = "mysql -h" + self.host +" "+ "-u" + self.user + " -p" + self.passwd + " " + self.db + " < " + self.backuppath +self.db+"-" + self.backupdate + ".sql"  # 还原数据库
            os.system(loadcmd)
            print('还原成功')
        except Exception as e:
            print(e.message)


if __name__=='__main__':
    a=MysqlHelper()
    card = int(input('请输入学号：'))
    sex = input('请输入性别：')
    sql_1 = "select age from stu where id>=%s and sex=%s"
    data1 = [card, sex]
    b=a.select(sql_1,data1)
    print(b)
    a.backup()

