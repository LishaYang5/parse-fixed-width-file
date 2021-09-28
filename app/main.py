'''
Author: your name
Date: 2021-09-28 13:15:14
LastEditTime: 2021-09-28 13:39:16
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /parse-fixed-width-file/app/main.py
'''
import csv

import sys
sys.path.append("..")
for i in sys.path:
     print(i)

from core import get_csv
from src import generate_csv
import parser
import testParser

def main(fileName):
    testParser.testParser(testCsv=fileName)
    
if __name__ == '__main__':
    fileName = 'test.csv'
    main(fileName)