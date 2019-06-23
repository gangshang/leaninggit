class global_var():
    Id = 0         #用例编号
    case_name=1    #用例名
    request_name =2#接口名
    url =3   #接口地址
    run =4   #是否运行
    request_way =5  #请求方式
    header =6#请求头
    case_depend =7#是否依赖
    data_depend =8#依赖的返回数据
    field_depend =9#依赖的字段
    data =10 #请求数据
    result_data=11#接口返回数据
    expect =12#预期结果
    result =13#测试结果

def get_id():
    return global_var.Id
#获取url
def get_url():
    return global_var.url

def get_run():
    return global_var.run

def get_run_way():
    return global_var.request_way

def get_header():
    return global_var.header

def get_case_depend():
    return global_var.case_depend

def get_data_depend():
    return global_var.data_depend

def get_field_depend():
    return global_var.field_depend

def get_data():
    return global_var.data
def get_result_data():
    return global_var.result_data
def get_expect():
    return global_var.expect
def get_result():
    return global_var.result
