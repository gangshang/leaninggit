#-*-coding:utf-8-*-
# author: wangjinqi
# date：2019-06-10

class Compare:
    def is_contain_str(self,str_one,str_two):
        '''判断一个字符串是否在另一个字符串中
        str_one--被判断的字符串
        str_two--作为比较的字符串
        '''
        flag = None
        if str_one in str_two:
            flag=True
        else:
            flag=False
        return flag
   # def is_contain_dict(self,items,dict2):


