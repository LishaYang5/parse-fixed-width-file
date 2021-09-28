'''
Author: Lisha Yang
Date: 2021-09-28 03:54:43
LastEditTime: 2021-09-28 15:06:30
Description: Build a parser to parse test data and source data(csv_par.csv)
FilePath: /parse-fixed-width-file/parser.py
'''
import csv
from core import get_csv

def parser(sampledata):
    # Get source data 
    fileName='csv_par.csv'
    parfile = get_csv.getCsv(csv_file=fileName)
    header = list(parfile[0].keys())

    # Compare new data width with parfile
    def comparValue(sampledata,col):
        if len(sampledata[0].get(col)) < len(parfile[0][col]):
            ad_num = len(parfile[0][col])-len(sampledata[0].get(col))
            sampledata[0][col] += ad_num * '*'

        if len(sampledata[0].get(col)) > len(parfile[0][col]):
            mi_num = len(parfile[0][col])
            sampledata[0][col] = sampledata[0][col][:mi_num]

    for col in header:
        comparValue(sampledata=sampledata, col=col)

    # Add parsed data into file
    parfile.extend(sampledata)

    try:
        with open('parsed.csv', 'w') as f:
            writer = csv.DictWriter(f, fieldnames=header)
            writer.writeheader()
            for elem in parfile:
                writer.writerow(elem)
    except IOError:
        print("I/O error")