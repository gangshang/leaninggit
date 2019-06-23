#-*-coding:utf-8-*-
# author: wangjinqi
# date：2019-06-10
from base import runmethod
from case import get_case
from utils.compare import Compare
from utils.sendemail import SendEmail
from log.mylog import MyLog
class RunTest:
    def __init__(self):
        self.run_method=runmethod.RunMethod()
        self.case=get_case.GetCase()
        self.compare=Compare()
        self.send_report=SendEmail()
        self.log=MyLog('RunTest')

    def go_on_test(self):
        run_list=[]#运行的案例
        pass_list=[]#通过的案例
        fail_list=[]#失败的案例
        rows=self.case.get_case_num()#获取总行数
        self.log.info('获取总行数')
        case_num=rows-1#总案例数
        self.log.info('总案例数')
        for i in range(1,rows):      #排除掉Excel第一行，所以从1开始循环
            method=self.case.get_request_method(i)
            #print(method)
            url=self.case.get_request_url(i)
            #print(url)
            is_run=self.case.get_is_run(i)
            #print(is_run)
            data=self.case.get_request_data(i)
            #print(data)
            header=self.case.get_is_header(i)
            #print(header)
            expect=self.case.get_expect_data(i)

            print(type(expect))
            print(expect)
            if is_run==True:
                run_list.append(i)#将运行的案例添加到列表
                res=self.run_method.run_main(method,url,data)
                print(type(res))
                print(res)
                self.case.write_result_data(i,res)#返回结果写到excel
                if self.compare.is_contain_str(expect,res):#比对预期结果和实际结果
                    self.case.write_result_test(i,'pass')
                    print('测试通过')
                    pass_list.append(i)#将通过的案例添加到列表
                else:
                    self.case.write_result_test(i,'fail')
                    print('测试失败')
                    fail_list.append(i)#将失败的案例添加到列表
        self.send_report.mail_report(case_num,pass_list,fail_list)#发送测试报告


if __name__=='__main__':
    a=RunTest()
    a.go_on_test()#调用对象方法

