'''
Author: your name
Date: 2021-09-28 03:47:46
LastEditTime: 2021-09-28 13:50:54
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /parse-fixed-width-file/generate_csv.py
'''
import csv

def geneCsv():
  labels = ['f1', 'f2', 'f3','f4','f5','f6','f7','f8','f9','f10']
  dct_arr = [
    {'f1':12345,'f2':123456789111 ,'f3': 123,'f4':22,'f5':1234567891234,'f6':1234567,'f7':1234567890,'f8':1234567891234,'f9':12345678901234567890,'f10':1234567891234},
  ]

  try:
      with open('csv_par.csv', 'w') as f:
          writer = csv.DictWriter(f, fieldnames=labels)
          writer.writeheader()
          for elem in dct_arr:
              writer.writerow(elem)
  except IOError:
      print("I/O error")