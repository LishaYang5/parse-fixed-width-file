'''
Author: your name
Date: 2021-09-25 01:11:41
LastEditTime: 2021-09-25 01:15:43
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /parse-fixed-width-file/t2.py
'''
import csv

headers = ['name','age','classroom']
values = [
    {"name":'wenn',"age":20,"classroom":'222'},
    {"name":'abc',"age":30,"classroom":'333'}
]
with open('t2.csv','w',newline='') as fp:
    writer = csv.DictWriter(fp)
    #writer = csv.writeheader()
    writer.writerow(headers)
    #writer.writerows(values)