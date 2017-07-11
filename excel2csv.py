#!/usr/bin/python2.7
# coding: utf8
import sys
import xlrd
import csv
import math
import types
from datetime import date,datetime,time

import sys  
reload(sys)  
sys.setdefaultencoding('utf8')
 
def csv_from_excel(xlsx_filepath, csv_filepath, sheet):
    # '''
    # excel转换函数
    # 将excel文件转换为文本文件
    # 包含旧版的.xls文件和新版的.xlsx文件
    # xlsx_filepath: 待转换文件路径
    # csv_filepath: 生成的文件路径
    # sheet: Excel中工作表索引，第一个工作表的索引为0，以此类推 默认为0
    # '''
    wb = xlrd.open_workbook(xlsx_filepath,encoding_override='utf-8')
    sh = wb.sheet_by_index(sheet)
    csv_file = open(csv_filepath, 'wb')
    wr = csv.writer(csv_file, quoting=csv.QUOTE_NONNUMERIC)
    nrows = sh.nrows
    ncols = sh.ncols

    for rownum in xrange(nrows):
        temp = []
        for colnum in xrange(ncols):
            cell = sh.cell(rownum, colnum)
            if cell.ctype is xlrd.XL_CELL_NUMBER:
                # if math.ceil(cell.value) == math.floor(cell.value) :
                #     temp.append(int(cell.value))
                # else:
                    temp.append(int(cell.value))
            else:
                temp.append(str(cell.value).encode('utf-8'))
        
        #将每行中的数据以Tab分隔
        # newrow = ','.join(temp)
        # wr.writerow([newrow])
        wr.writerow(temp)

    csv_file.close()

if __name__ == "__main__":
    if len(sys.argv) <= 4:
        if len(sys.argv) == 3:
            seet = 0
        else:
            seet = int(sys.argv[3])

        csv_from_excel(sys.argv[1], sys.argv[2],seet)
    else:
        # print '参数不正确'
        sys.exit(1)
