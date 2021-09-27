'''
Author: your name
Date: 2021-09-27 12:04:12
LastEditTime: 2021-09-27 12:13:27
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /parse-fixed-width-file/app/core/get_row.py
'''
def getRows(rowsCombine,rowLen):
    index = 0
    totalRow = []
    for rows in rowsCombine:
        rows.extend(int(rowLen[index])*[rowLen[index]])
        totalRow.append(rows)
        index +=1
    return totalRow 