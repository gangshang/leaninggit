#-*-coding:utf-8-*-
# author: wangjinqi
# date：2019-06-10

from utils import operationexcel
from case import case_config
from utils import readjson
class GetCase():
    def __init__(self):
        self.tables=operationexcel.OperationExcel('用例.xls',0)
        self.opera_json=readjson.ReadJson()
    '''获取总行数，也就是案例数'''
    def get_case_num(self):
        return self.tables.get_lines()
    # 获取是否执行
    def get_is_run(self,row):
        flag=None
        col=case_config.get_run()
        run=self.tables.get_cell_value(row,col)
        if run=='yes':
            flag=True
        else:
            flag=False
        return flag

    # 是否携带header
    def get_is_header(self,row):
        col=case_config.get_header()
        header=self.tables.get_cell_value(row,col)
        if header !='':
            return header
        else:
            return None

    # 获取请求方式
    def get_request_method(self,row):
        col=case_config.get_run_way()
        request_method=self.tables.get_cell_value(row,col)
        return request_method

    # 获取url
    def get_request_url(self, row):
        col = case_config.get_url()
        url = self.tables.get_cell_value(row, col)
        return url
    #获取请求数据
    def get_request_data(self,row):
        col=case_config.get_data()
        data=self.tables.get_cell_value(row,col)
        if data !='':
            data_json=self.opera_json.get_json(data)
            return data_json
        else:
            return None
    #获取预期结果
    def get_expect_data(self,row):
        col=case_config.get_expect()
        expect=self.tables.get_cell_value(row,col)
        return expect
    #写入接口返回数据
    def write_result_data(self,row,vaule):
        col=case_config.get_result_data()
        self.tables.write_vaule(row,col,vaule)
    #写入测试结果
    def write_result_test(self,row,vaule):
        col=case_config.get_result()
        self.tables.write_vaule(row,col,vaule)



if __name__=='__main__':
    a=GetCase()
    print(a.get_case_num())
    print(a.get_is_run(1))
    print(a.get_request_method(1))
    print(a.get_request_url(1))
    print(a.get_is_header(1))
    print(a.get_expect_data(1))
    print(a.get_request_data(1))





