import xlrd
from config import readconfig
import os
from xlutils.copy import copy
'''
fp=readconfig.ReadConfig()
fp1=fp.get_excel('excel')
print(fp1)
fp2=os.path.join(fp1,'用例.xlsx')
print(fp2)
data=xlrd.open_workbook(fp2)
print(data)
table=data.sheets()[0]
print(table)
nrows=table.nrows
ncols=table.ncols
print(nrows)
print(ncols)
row_data=table.row_values(0)
print(row_data)
cow_data=table.col_values(0)
print(cow_data)
cell_value=table.cell_value(1,3)
print(cell_value)
'''
class OperationExcel():
    def __init__(self,file_name='用例.xls',sheet_id=0):
        fp = readconfig.ReadConfig().get_excel('excel')#获取Excel存放地址
        self.fp1 = os.path.join(fp,file_name)#组装要打开的exc的路径
        self.sheet_id=sheet_id
        self.tables=self.get_data()

        '''获取sheet内容'''
    def get_data(self):
        data=xlrd.open_workbook(self.fp1)
        tables=data.sheets()[self.sheet_id]
        return tables

    '''获取sheet的总行数'''
    def get_lines(self):
        rows=self.tables.nrows
        return rows

    '''根据行号、列号获取单元格数据'''
    def get_cell_value(self,row,col):
        cell_value=self.tables.cell_value(row,col)
        return cell_value

    '''写入数据'''
    def write_vaule(self,row,col,value):
        read_data=xlrd.open_workbook(self.fp1,formatting_info=True)#formatting_info=True保留原有格式
        write_data=copy(read_data)#转化为可追加写入模式，复制文件
        sheet_data=write_data.get_sheet(self.sheet_id)#获取sheet数据
        sheet_data.write(row,col,value)#写入单元格
        write_data.save(self.fp1)#保存，只支持.xls文件






if __name__=='__main__':
    a=OperationExcel()
    b=a.get_lines()
    print(b)
    c=a.get_cell_value(1,13)
    print(c)
    a.write_vaule(2,13,'测试2')
