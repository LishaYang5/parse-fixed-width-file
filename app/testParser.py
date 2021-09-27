'''
Author: your name
Date: 2021-09-28 04:13:51
LastEditTime: 2021-09-28 06:05:01
Description: Test parser
FilePath: /parse-fixed-width-file/app/test.py
'''
import csv
import parser
from core import get_csv

if __name__ == '__main__':
    fileName = 'test.csv'
    sampledata = get_csv.getCsv(csv_file=fileName)
    parser.parser(sampledata=sampledata)