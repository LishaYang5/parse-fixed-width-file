'''
Author: Lisha Yang
Date: 2021-09-28 13:15:14
LastEditTime: 2021-09-28 17:33:26
Description: The access of the app
FilePath: /parse-fixed-width-file/app/main.py
'''
import sys
sys.path.append("..")
for i in sys.path:
     print(i)
import csv
from core import get_csv
from src import generate_csv
import parser
import testParser

def main(fileName):
    testParser.testParser(testCsv=fileName)
    
if __name__ == '__main__':
    # Generate csv file
    generate_csv.geneCsv()
    
    # Use test csv file to test parser and generete a parsed file
    fileName = 'test.csv'
    main(fileName)