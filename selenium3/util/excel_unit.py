#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/18 0018 10:40
# @Author  : Aries
# @Site    : 
# @File    : excel_unit.py
# @Software: PyCharm
from xlutils.copy import copy
import xlrd
import xlwt


class ExcelUtil:
    def __init__(self, excel_path=None, index=None):
        if excel_path is None:
            self.excel_path = 'C:\\Users\\Administrator\\PycharmProjects\\selenium3\\config\\keyword.xls'
        else:
            self.excel_path = excel_path
        if index is None:
            index = 0
        # 整个表格
        self.data = xlrd.open_workbook(self.excel_path)
        self.table = self.data.sheets()[index]

    # 获取excel数据
    def get_data(self):
        result = []
        if self.get_lines() is None:
            return None
        for i in range(self.get_lines()):
            col = self.table.row_values(i)
            col[0] = str(int(col[0]))
            result.append(col)
        return result

    # 获取Excel行数
    def get_lines(self):
        rows = self.table.nrows
        if rows >= 1:
            return rows
        return None

    # 获取单元格的数据
    def get_col_value(self, row, col):
        if self.get_lines() > row:
            data = self.table.cell(row, col).value
            if isinstance(data, float):
                data = str(int(data))
            return data
        return None

    # 写入数据
    def write_value(self, row, value):
        read_value = xlrd.open_workbook(self.excel_path)
        write_data = copy(read_value)
        write_data.get_sheet(0).write(row, 9, value)
        write_data.save(self.excel_path)


# if __name__ == '__main__':
#     ExcelUtil().write_value(0, 'success')
