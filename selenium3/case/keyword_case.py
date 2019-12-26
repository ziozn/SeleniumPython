#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/19 0019 15:21
# @Author  : Aries
# @Site    : 
# @File    : keyword_case.py
# @Software: PyCharm
from util.excel_unit import ExcelUtil
from keywordSelenium.actionMethod import ActionMethod


class KeyWordCase:
    def run_main(self):
        self.action_method = ActionMethod()
        handle_execl = ExcelUtil('C:\\Users\\Administrator\\PycharmProjects\\selenium3\\config\\keyword.xls')
        case_lines = handle_execl.get_lines()
        if case_lines is not None:
            for i in range(1, case_lines):
                is_run = handle_execl.get_col_value(i, 3)
                if is_run == 'yes':
                    # 需要执行的方法
                    method = handle_execl.get_col_value(i, 4)
                    # 需要输入的数据
                    send_value = handle_execl.get_col_value(i, 5)
                    # 需要操作的元素
                    handle_value = handle_execl.get_col_value(i, 6)
                    # 预期结果方法
                    except_result_method = handle_execl.get_col_value(i, 7)
                    # 预期结果值
                    except_result = handle_execl.get_col_value(i, 8)
                    self.run_method(method, send_value, handle_value)
                    if except_result != '':
                        except_value = self.get_except_result_value(except_result)
                        if except_value[0] == 'text' and except_value[1] in self.run_method_result(except_result_method):
                            handle_execl.write_value(i, 'pass')
                        elif except_value[0] == 'login':
                            handle_execl.write_value(i, 'pass')
                        else:
                            handle_execl.write_value(i, 'fail')

    # 获取预期结果值
    @staticmethod
    def get_except_result_value(data):
        return data.split('=')

    #                    方法名 ， 输入参数，     操作的元素
    def run_method(self, method, send_value='', handle_value=''):
        method_value = getattr(self.action_method, method)
        if send_value != '':
            method_value(send_value, handle_value)
        elif send_value == '' and handle_value == '':
            method_value()
        else:
            method_value(handle_value)

    # 结果断言
    def run_method_result(self, method):
        method_value = getattr(self.action_method, method)
        result = method_value()
        return result


if __name__ == '__main__':
    KeyWordCase().run_main()

