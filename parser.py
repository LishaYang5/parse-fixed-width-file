'''
Author: Lisha Yang
Date: 2021-09-24 16:21:11
LastEditTime: 2021-09-25 00:56:49
Description: In User Settings Edit
FilePath: /parse-fixed-width-file/parser.py
'''
import json
import csv
filename = 'spec.json'

def getHeader():
    with open(filename) as f:
        pop_data = json.load(f)
        return pop_data.get('ColumnNames',-1)

def getRowLen():
    with open(filename) as f:
        pop_data = json.load(f)
        return pop_data.get('Offsets',-1)

header = []
header = getHeader()

rowLen = []
rowLen = getRowLen()

# generate specific numbers of rows based on the header's lenth
rowsCombine = []
for i in range(len(header)):
    rows = 'list%s'%i
    rows = []
    rowsCombine.append(rows)

def getRows():
    index = 0
    totalRow = []
    for rows in rowsCombine:
        rows.extend(int(rowLen[index])*[''])
        totalRow.append(rows)
        index +=1
    return totalRow 

totalRows = getRows()

with open('spec.csv','w') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(header)
    for r in totalRows:
        f_csv.writerow(r)