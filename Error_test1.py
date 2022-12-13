'''
@File    :   Error_test1.py
@Contact :   xwz3568@163.com

@Modify Time          @Author    @Version    @Desciption
------------          --------   --------    -----------
2022/10/16 0016 9:59  FuGui      1.0         None
'''

#
# class NewError(Exception):
#     def __init__(self, message):
#         self.message = message
#
#
# def test():
#     raise NewError('这是一个自定义异常')
#
#
# try:
#     test()
# except NewError as e:
#     print(e)


import csv

with open(r"C:\Users\Administrator\Desktop\BigData\数据集及要求\数据集1_电影数据\电影数据.csv") as c:
    csT = csv.reader(c)
    column3 = [row[2] for row in csT]  #列表推导式
    for i in column3:
        a = i.replace("|",",")
        print(a)





































































