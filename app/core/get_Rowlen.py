'''
Author: your name
Date: 2021-09-27 11:56:59
LastEditTime: 2021-09-27 11:59:30
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /parse-fixed-width-file/app/core/get_Rowlen.py
'''
import json
def getRowLen(fn):
    try:
        with open(fn) as f:
            pop_data = json.load(f)
    except IOError:
        print('Cannot get file')
    else:
        return pop_data.get('Offsets',-1)