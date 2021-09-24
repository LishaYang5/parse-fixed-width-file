'''
Author: your name
Date: 2021-09-25 00:49:14
LastEditTime: 2021-09-25 01:07:20
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /parse-fixed-width-file/test.py
'''
import csv

#先给data赋值
data1 = [1,2,3,4]
data2 = [5,6,7]
with open('spec.csv','r') as csvFile:  #此处的csv是源表，即想要写入的表
    reader = csv.reader(csvFile)
    titles = next(reader)
    for x in reader:
        print(x)
    '''
    with open('2.csv','w',newline='') as f: #这里的csv则是最后输出得到的新表
        writer = csv.writer(f)
        
        
        
        i = 0
        for row in rows:
            row.append(data[i])
            print(i)
            i = i + 1
            writer.writerow(row)'''
