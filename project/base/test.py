import time
a={'a':1,'b':2,'d':3}
b="'status': 10006"
print(type(b))
print(b)
for item in a.items():

    print(type(item))
    print(item)
now = time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime(time.time()))
sub = '接口自动化回归测试报告'+"_"+now
print(sub)
v=[1,23,3,34]
m="失败编号为%s。"%v
print(m)
print(v)
print(1)