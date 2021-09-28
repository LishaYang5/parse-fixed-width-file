'''
Author: Lisha Yang
Date: 2021-09-28 04:05:05
Description: Create an object that operates like a regular reader
            but maps the information in each row to a 
            dict whose keys are given by the optional fieldnames parameter.
FilePath: /parse-fixed-width-file/app/core/get_file.py
'''
import csv

def getCsv(csv_file):
    with open(csv_file,'r') as f:
        reader = csv.DictReader(f)
        rows = [row for row in reader]
        return rows