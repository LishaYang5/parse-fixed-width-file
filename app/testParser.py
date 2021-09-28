'''
Author: Lisha Yang
Date: 2021-09-28 04:13:51
LastEditTime: 2021-09-28 15:06:39
Description: Test parser
FilePath: /parse-fixed-width-file/app/test.py
'''
import csv
import parser
from core import get_csv

def testParser(testCsv):
    sampledata = get_csv.getCsv(csv_file=testCsv)
    parser.parser(sampledata=sampledata)