import tablib
import numpy
import pandas as pd
file1=pd.read_csv('/home/washingli/文档/1.csv',encoding='utf-8')  #file1是今天的数据
file2=pd.read_csv('/home/washingli/文档/2.csv',encoding='utf-8')   #file2是昨天的数据
# 读写行和列
# print(file1.head())
# print(file1['标题'])
# print(file1.icol(0,1))
# print(file1.icol(0:1,1))


# print(file1)
list=[]
for i in file1.index:
    for m in file2.index:
        if(file1.loc[i,'地点']==file2.loc[m,'地点']):
            # file=file1.drop(i)
            list.append(i)
        else:
            continue
# print(file1)
# file=file1['地点']!=file2['地点']
file=file1.drop(list)
print(file)
file.to_csv('/home/washingli/文档/3.csv')

