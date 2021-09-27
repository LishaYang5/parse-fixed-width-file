'''
Author: Lisha Yang
Date: 2021-09-24 16:21:11
LastEditTime: 2021-09-27 12:14:27
Description: The parser is to generate a csv file, which has 10 columns 
            and specific numbers of values in each column.
FilePath: /parse-fixed-width-file/parser.py
'''
import json
import csv
from core import get_header
from core import get_Rowlen
from core import get_row

def main():
    filename = 'spec.json'
    
    # Get header of csv file
    header = []
    header = get_header.getHeader(filename=filename)
    
    # Get value of length for each column
    rowLen = []
    rowLen = get_Rowlen.getRowLen(fn=filename)
    
    # generate specific numbers of rows based on the header's lenth
    rowsCombine = []
    for i in range(len(header)):
        rows = 'list%s'%i
        rows = []
        rowsCombine.append(rows)
        
    # Get totalRows for csv
    totalRows = get_row.getRows(rowsCombine=rowsCombine,rowLen=rowLen)
    
    # Assign row values for each column based on the length
    f1=totalRows[0]
    f2=totalRows[1]
    f3=totalRows[2]
    f4=totalRows[3]
    f5=totalRows[4]
    f6=totalRows[5]
    f7=totalRows[6]
    f8=totalRows[7]
    f9=totalRows[8]
    f10=totalRows[9]
    
    # get longest length and make every column has same length
    max_len=max(len(f1),len(f2),len(f3),len(f4),len(f5),len(f6),len(f7),len(f8),len(f9),len(f10))
    add_f1=max_len-len(f1)
    add_f2=max_len-len(f2)
    add_f3=max_len-len(f3)
    add_f4=max_len-len(f4)
    add_f5=max_len-len(f5)
    add_f6=max_len-len(f6)
    add_f7=max_len-len(f7)
    add_f8=max_len-len(f8)
    add_f9=max_len-len(f9)
    add_f10=max_len-len(f10)

    # add empty value in each column
    f1.extend(add_f1*[''])
    f2.extend(add_f2*[''])
    f3.extend(add_f3*[''])
    f4.extend(add_f4*[''])
    f5.extend(add_f5*[''])
    f6.extend(add_f6*[''])
    f7.extend(add_f7*[''])
    f8.extend(add_f8*[''])
    f9.extend(add_f9*[''])
    f10.extend(add_f10*[''])

    #generate csv file
    rows = zip(f1,f2,f3,f4,f5,f6,f7,f8,f9,f10)
    with open('spec.csv','w',newline='',encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile,delimiter=',')
        writer.writerow(header)
        writer.writerows(rows)

if __name__ == '__main__':
    main()