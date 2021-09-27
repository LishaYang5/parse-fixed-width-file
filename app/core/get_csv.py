'''
Author: your name
Date: 2021-09-28 04:05:05
LastEditTime: 2021-09-28 05:51:05
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /parse-fixed-width-file/app/core/get_file.py
'''
import csv

def getCsv(csv_file):
    with open(csv_file,'r') as f:
        reader = csv.DictReader(f)
        rows = [row for row in reader]
        return rows