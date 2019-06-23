#-*-coding:utf-8-*-
# author: wangjinqi
# date：2019-06-05

import requests
import json


class RunMethod():
    '''发送接口请求方法类'''
    '''发送get请求'''
    def get_request(self,url,data=None,header=None):
        res=requests.get(url=url,data=data,headers=header)
        return res.json()
    '''发送post请求'''
    def post_request(self,url,data,header=None):
        res=requests.post(url=url,data=data,headers=header,verify=False) # HTTPS请求需要加参数verify=False
        return res.json()
    '''请求主方法'''
    def run_main(self,method,url,data=None,header=None):
        res=None
        if method=='get':
            res=self.get_request(url=url,data=data,header=header)
        if method=='post':
            res=self.post_request(url=url,data=data,header=header)
        #return res.text.encode('utf-8').decode('unicode_escape')#防止中文乱码
        return json.dumps(res)

        '''
        if res.content:              # 判断是否有返回，有则将返回结果转为json格式
            return res
        else:
            return res.status_code  # 返回请求状态码
        '''
if __name__ == '__main__':
    url='https://access.video.qq.com/user/auth_login?vappid=11059694&vsecret=fdf61a6be0aad57132bc5cdf78ac30145b6cd2c1470b0cfe&raw=1&type=qq&appid=101483052&code=E247A294AEB34AE501618F0E450CCEF1'
    data={
        "timestamp": "1507272377898",
        "uid": "5249191",
        "uuid": "5ae7d1a22c82fb89c78f603420870ad7",
        "secrect": "7d33829ecc354f0b4e00fb3764cb4207",
        "marking": "androidbanner",
        "type": "1",
        "token": "50609fd5ffd05c734195d4bbc8dd5092"
    }
    test=RunMethod()
    a=test.run_main(method='get',url=url)
    print(type(a))
    print(a)





