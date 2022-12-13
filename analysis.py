'''
@File    :   analysis.py
@Contact :   xwz3568@163.com

@Modify Time          @Author    @Version    @Desciption
------------          --------   --------    -----------
2022/10/16 0016 14:40  FuGui      1.0        可视化（类型数量、评分8+、类型词云、不同年份电影数量，评分收入关系，评分收入top10）
'''
#C:\Users\Administrator\Desktop\BigData\数据集及要求\数据集1_电影数据
#路径用r"url"，语义为当前字符串中所有的\都转义
#关于词云图自定义形状无效：为自定义图片添加颜色模式属性，rgb或CMYK
# https://blog.csdn.net/weixin_39541693/article/details/110434307
#颜色模式RGB自身发光显示颜色，cmyk，百度了解，外部光源，靠反射显示，深色吸收不显示（是这样吗）
#如果这样，原有高对比度图片颜色要反转，无色区域显示字


import jieba
from wordcloud import WordCloud        #安装时可能缺少vc++开发环境，详见开发日志
import imageio    #背景轮廓图片 词云背景图：格式png，无色区域无字  [后续有改动]
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['Simhei']    #解决不能显示中文的问题

#对类型.txt做词频统计即可得到不同类型电影的数量，对类型top5和last3做柱状图可视化
def num_type():
    print("电影类型分析……")
    # 获取类型源数据
    txt = open(r"C:\Users\Administrator\Desktop\BigData\数据集及要求\数据集1_电影数据\类型.txt", "r").read()
    words = jieba.lcut(txt)

    dic = {}  # 定义一个空字典，用于词频键值对  {键:值}   {类型：次数}
    for word in words:
        if len(word) == 1:  # 单个词语不计算在内 剔除文本中的‘ ’分割符
            continue
        else:
            # 遍历所有词语，每出现一次其对应的值加 1
            dic[word] = dic.get(word, 0) + 1  # dict.get(word,0)获取字典对应键的值，如果不存在则返回0 存在则+1
            #词频统计详解：https://cloud.tencent.com/developer/article/1991537
    print("共{0}类电影,各类型数量分别为：{1}".format(len(dic),dic))  #map（）。reduce（）+1

    #由于数据过多，只可视化top5 last3并一起展示
    # 字典内排序使用内置函数sorted(迭代对象，【参与比较的对象】，排序顺序)     默认参数【比较对象】  结果是一个排好序的列表
    # reverse=true则是倒序(大->小)，reverse=false时则是顺序(小->大)
    # zip函数，用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表
    temp = sorted(zip(dic.values(), dic.keys()), reverse=True)
    # print(temp)  # 这里将值作为从大到小的排序依据，把值，键打包为一个个元组列表输出
    # 字典/列表推导式：按定义式运算，最后格式为字典/列表

    # 存放top5与last3 top1:max(dict.values())
    key = [item[1] for item in temp]
    last_key = key[-3:]  # 负值索引
    top_key = key[0:5]

    value = [item[0] for item in temp]
    last_value = value[-3:]
    top_value = value[0:5]

    # print(top_key) #['Drama', 'Action', 'Comedy', 'Adventure', 'Thriller']
    # print(top_value) #[438, 286, 254, 252, 152]
    # print(last_key) #['War', 'Western', 'Musical']
    # print(last_value) #[10, 5, 5]

    #绘制类型柱状图
    x= top_key+last_key
    num = top_value+last_value
    plt.bar(x=x, height=num)
    plt.title('电影类型统计柱状图')
    plt.show()



#统计评分在8以上的电影(包括8分)
def score():
    txt = open(r"C:\Users\Administrator\Desktop\BigData\数据集及要求\数据集1_电影数据\名分字典.txt", "r").read()
    txt = eval('{' +txt+ '}')  #转换为字典格式
    # print(type(txt))
    #将满足评分8+的电影存放在name列表中
    name = []
    for key,value in txt.items():
        temp = float(value)
        if temp >= 8:
            name.append(key)
        else:
            continue
    # print(name)
    #将结果每五个一行输入至控制台(可选是否保存本地)【能否上传云端或存至数据库】
    print("满足评分8+条件的共{}部电影,分别为：".format(len(name)))
    count = 0 #定义一个计数器来控制输出换行
    for n in name:
        count+=1
        if count%6==0:  #每5个换行
            print()
        else:
            print(n,end="  ")
            # #保存本地（选）
            # with open(r"C:\Users\Administrator\Desktop\BigData\数据集及要求\数据集1_电影数据\8分电影.txt", "a") as w:
            #     w.write(n + ' ')



#电影类型词云图  控制台展示及保存本地
def typecloud():
    img = imageio.imread_v2(r"C:\Users\Administrator\Desktop\BigData\数据集及要求\数据集1_电影数据\CloudImg.png",pilmode="CMYK")
    txt = open(r"C:\Users\Administrator\Desktop\BigData\数据集及要求\数据集1_电影数据\类型.txt", "r").read()
    #设置生成的词云参数 白色背景宽高800 自定义背景图
    wc = WordCloud(background_color="white",
                   width=800,
                   height=800,
                   mask=img,
                   )
    # 传入数据，将对象赋给wcloud  调用wrodcloud库的方法保存本地
    wcloud = wc.generate(txt)
    wcloud.to_file(r'C:\Users\Administrator\Desktop\BigData\数据集及要求\数据集1_电影数据\wordcloud.png') #保存到本地
    print("词云图片已保存")

    #控制台展示
    plt.imshow(wcloud)  # 使用plt库显示图片
    plt.axis("off")   # 矩形图表区域内不显示xy轴
    plt.show()




if __name__ == '__main__':
    #类型
    num_type()
    #评分8+
    score()
    #类型词云
    typecloud()