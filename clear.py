'''
@File    :   clear.py    
@Contact :   xwz3568@163.com

@Modify Time          @Author    @Version    @Desciption
------------          --------   --------    -----------
2022/10/16 0016 8:36  FuGui      1.0         数据清洗、生成新的csv
'''
#C:\Users\Administrator\Desktop\BigData\数据集及要求\数据集1_电影数据


import csv

#数据清洗，包含读取原始数据集，清洗后另存为新的数据集
def clear():
    with open(r"C:\Users\Administrator\Desktop\BigData\数据集及要求\数据集1_电影数据\电影数据.csv") as c:
        csv_all = csv.reader(c)
        csv_row = [row for row in csv_all]  # 列表推导式 详细百度
        print("开始清洗文件")
        print("开始另存数据……")
        i = 1  # 定义计数器，跳过表头读取数据
        for r in csv_row:
            if i != 1:
                if (r[1] != '') and (len(r[3]) == 4) and (r[6] != ''):  # 特别 1名称和6收入为‘’不是None，当同时满足时为合法数据写入新的csv
                    replace = r[2].replace("|", ",")
                    # print([r[1], replace, r[3], r[4], r[5],r[6]])
                    with open(r"C:\Users\Administrator\Desktop\BigData\数据集及要求\数据集1_电影数据\电影数据clear.csv",
                              "a", newline="", encoding="utf-8") as f:
                        csvwrite = csv.writer(f)
                        csvwrite.writerow([r[1], replace, r[3], r[4], r[5], r[6]])  # 写入时 格式必须为列表


                    #将每列单独另存为一个文本，方便后续做分析
                    with open(r"C:\Users\Administrator\Desktop\BigData\数据集及要求\数据集1_电影数据\类型.txt", "a") as w:
                        w.write(replace + ' ')
                    with open(r"C:\Users\Administrator\Desktop\BigData\数据集及要求\数据集1_电影数据\名称.txt", "a") as w:
                        w.write('《' + r[1] + '》' + ' ')
                    with open(r"C:\Users\Administrator\Desktop\BigData\数据集及要求\数据集1_电影数据\评分.txt", "a") as w:
                        w.write(r[5] + ' ')
                    with open(r"C:\Users\Administrator\Desktop\BigData\数据集及要求\数据集1_电影数据\收入.txt", "a") as w:
                        w.write(r[6] + ' ')
                    with open(r"C:\Users\Administrator\Desktop\BigData\数据集及要求\数据集1_电影数据\年份.txt", "a") as w:
                        w.write(r[3] + ' ')
                    with open(r"C:\Users\Administrator\Desktop\BigData\数据集及要求\数据集1_电影数据\名分字典.txt", "a") as w:
                        w.write('"《' + r[1] + '》"' + ':"' + r[5] + '",\n') #添加字典格式
                else:
                    continue
            i += i
        print("文件另存完成")
        print("文件清洗完成")


if __name__ == '__main__':

    #准备csv文件,写入首行标题
    with open(r"C:\Users\Administrator\Desktop\BigData\数据集及要求\数据集1_电影数据\电影数据clear.csv",
              "a", newline="", encoding="utf-8") as f:
        csvwrite = csv.writer(f)
        csvwrite.writerow(["名称","类型","上映时间","片长","评分","收入(百万)"]) #为后续使用tableau可视化做准备

    #调用清洗函数
    clear()
