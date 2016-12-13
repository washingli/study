import pandas as pd
file=pd.read_csv('/home/washingli/文档/famingren.csv','coding=utf-8')

for m in file.index:    #m control index
    i=1
    speople=str(file.loc[m,'发明人'])
    speople=speople.split(' ')
    for n in speople:     #n control every people
        file.loc[m,'发明人'+str(i)]=n
        i=i+1
print(file)
