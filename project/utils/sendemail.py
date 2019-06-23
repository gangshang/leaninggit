#-*-coding:utf-8-*-
# author: wangjinqi
# date：2019-06-15
import smtplib
from email.mime.text import MIMEText
import time

class SendEmail:
    global mail_host
    global mail_user
    global mail_pass
    mail_host = "smtp.qq.com"#邮件服务器
    mail_user = "464787796@qq.com"#发件邮箱
    mail_pass = "nlapungitbrucaaj"#发件邮箱密码
    def send_email(self,mail_list,sub,content):
        '''
        构造邮件并发送
        :param mail_list: 发送列表
        :param sub: 主题
        :param content: 内容
        :return:
        '''
        user=mail_user+"<"+mail_user+">"#发件人
        message=MIMEText(content,_subtype='plain',_charset='utf-8')#构造邮件
        message['Subject']=sub#主题
        message['From']=user#发送人
        message['To']=';'.join(mail_list)#收件人
        server = smtplib.SMTP()
        server.connect(mail_host)#连接服务器
        server.login(mail_user,mail_pass)#登录
        server.sendmail(user, mail_list, message.as_string())#发送
        server.close()#关闭

    def mail_report(self,case_num,pass_list,fail_list):
        '''
        构建测试邮件报告模板
        :param case_num: 总案例数
        :param pass_list: 通过的案例列表
        :param fail_list: 失败的案例列表
        :return:
        '''
        pass_count=len(pass_list)#通过个数
        fail_count=len(fail_list)#失败个数
        run_count=pass_count+fail_count#运行总数
        pass_result="%.2f%%"%(float(pass_count)/run_count*100)#成功率
        fail_result="%.2f%%"%(float(fail_count)/run_count*100)#失败率
        mail_list = ['1315095608@qq.com']
        now = time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime(time.time()))
        sub = "接口自动化回归测试报告" + "_" + now
        content = "接口总案例数为%s个，此次回归一共运行接口案例个数为%s个，通过个数为%s个，" \
                  "通过率为%s,失败个数为%s,失败率为%s，失败的案例编号为%s。" \
                  %(case_num,run_count,pass_count,pass_result,fail_count,fail_result,fail_list)
        self.send_email(mail_list,sub,content)


if __name__ == '__main__':
    a=SendEmail()
    mail_list=['1315095608@qq.com']
    sub='接口测试报告'
    content='测试邮件'
    a.send_email(mail_list,sub,content)
    pass_list=[1,2,3,7,9,8]
    fail_list=[4,5,6]
    a.mail_report(pass_list,fail_list)

