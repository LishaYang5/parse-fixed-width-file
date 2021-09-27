'''
Author: your name
Date: 2021-09-27 11:52:13
LastEditTime: 2021-09-27 11:56:18
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /parse-fixed-width-file/app/get_header.py
'''
import json 
def getHeader(filename):
    try:
        with open(filename) as f:
            pop_data = json.load(f)
    except IOError:
        print("Cannot get file")
    else:    
        return pop_data.get('ColumnNames',-1)