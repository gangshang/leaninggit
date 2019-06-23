#-*-coding:utf-8-*-
# author: wangjinqi
# date：2019-06-05
import logging
import os
import time
#日志级别： debug < info < warning < error < critical
'''
logging.debug('debug级别，最低级别，一般开发人员用来打印一些调试信息')
logging.info('info级别，正常输出信息，一般用来打印一些正常的操作')
logging.warning('waring级别，一般用来打印警信息')
logging.error('error级别，一般用来打印一些错误信息')
logging.critical('critical 级别，一般用来打印一些致命的错误信息,等级最高')

logging.basicConfig(format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s',
                    level=logging.DEBUG)
print(os.getcwd())
'''

cur_path = os.path.dirname(os.path.realpath(__file__))
print(cur_path)
log_path = os.path.join(os.path.dirname(cur_path), 'logs')
print(log_path)
# 如果不存在这个logs文件夹，就自动创建一个
if not os.path.exists(log_path):os.mkdir(log_path)
class MyLog():

    def __init__(self,name):
        # 文件的命名
        self.logname = os.path.join(log_path, '%s.log' % time.strftime('%Y_%m_%d'))
        print(self.logname)
        self.logger = logging.getLogger(name)#获取日志
        self.logger.setLevel(logging.DEBUG)#设置日志的最低输出等级
        # 日志输出格式
        self.formatter = logging.Formatter('[%(asctime)s] -%(filename)s- %(name)s] - %(levelname)s: %(message)s')

    def __console(self, level, message):
        # 创建一个FileHandler，用于写到本地
        fh = logging.FileHandler(self.logname, 'a', encoding='utf-8')  # 这个是python3的
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)

        # 创建一个StreamHandler,用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)

        if level == 'info':
            self.logger.info(message)
        elif level == 'debug':
            self.logger.debug(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)
        # 这两行代码是为了避免日志输出重复问题
        self.logger.removeHandler(ch)
        self.logger.removeHandler(fh)
        # 关闭打开的文件
        fh.close()

    def debug(self, message):
        self.__console('debug', message)

    def info(self, message):
        self.__console('info', message)

    def warning(self, message):
        self.__console('warning', message)

    def error(self, message):
        self.__console('error', message)

if __name__ == '__main__':
    log=MyLog()
    log.error('cs ')
