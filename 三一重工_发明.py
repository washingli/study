#  coding=utf-8

import pandas as pd

# Read a CSV file
def ReadCSV(paths):
    try:
        brics = pd.read_csv(paths, encoding='utf-8')
    except:
        brics = pd.read_csv(paths, encoding='gbk')
    return brics


def Splitsw(f_path):
    bricsw = ReadCSV(f_path)
    for linesw in bricsw.index:
        i = 1
        str_line = str(bricsw.loc[linesw, '发明人'])
        str_line = str_line.split(' ')
        for namesw in str_line:
            bricsw.loc[linesw, '发明人' +str(i)] = namesw
            # print(bricsw.loc[linesw, '发明人' + str(i)])
            i=i+1
    print(bricsw)
    return bricsw

        # print(str_line)
        # print(len(str_line))


if __name__ == '__main__':
    realpath = "C:\\Users\\东旭\\Desktop\\三一重工-发明2016-12-08 16-44-11.csv"
    data = Splitsw(realpath)
    data.to_csv('C:\\Users\\东旭\\Desktop\\三一重工-发明.csv')
