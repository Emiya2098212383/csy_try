# -*- coding: UTF-8 -*-

# Filename : 01-string.py
# author by : Emiya

import csv
import os


# Global: Define file name & path
filename = 'test_write.csv'
csv_path = os.getcwd() + '\\csv_files\\' + filename


# Practice 1  - write
# write a row once
header_data = ["1行号", "2列名1", "3列名2"]
row_data = [1, '第1列数据', '第2列数据']  # data of a row
with open(csv_path, "w", encoding='utf8', newline='') as csvfile:
    writer = csv.writer(csvfile)
    #writer.writerow(header_data)
    #writer.writerow(row_data)
    for i in range(10):
        #writer.writerow(row_data)
        writer.writerow(header_data)

# Practice 3 - get filed(cell)
with open(csv_path, "r", encoding='utf8') as csvfile:
    reader = csv.reader(csvfile)
    row_cnt = 0
    for line in reader:
        row_cnt += 1
        print('第 %d 行， 行号是 %s, 第一列是 %s, 第二列是 %s' %
              (row_cnt, line[0], line[1], line[2]))
