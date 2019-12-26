#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/13 0013 14:55
# @Author  : Aries
# @Site    : 
# @File    : unittest_data_ddt_test.py
# @Software: PyCharm
import ddt
from business.register_business import RegisterBusiness
from selenium import webdriver
import time
import unittest
import os
import HTMLTestRunner
from util import excel_unit
data = excel_unit.ExcelUtil().get_data()


# 这里可以验证各种case，比如账号长度不合格，密码长度不合格。目前所用的只是两条较为简单的登陆成功以及失败的case
@ddt.ddt
class FirstCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('所有case执行之前的前置')

    @classmethod
    def tearDownClass(cls):
        print('所有case执行之后的后置')

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://login.taobao.com/member/login.jhtml')
        self.driver.maximize_window()
        time.sleep(1)
        self.login = RegisterBusiness(self.driver)

    def tearDown(self):
        time.sleep(2)
        for method_name, error in self._outcome.errors:
            if error is not None:
                case_name = self._testMethodName
                img_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
                img_path = os.path.join(img_path, 'img', case_name + '.png')
                self.driver.save_screenshot(img_path)
        self.driver.close()

    # 账号检验不成功
    @unittest.skip('0000')
    def test_login_user_error(self):
        print('aaa')
        pass

    # 密码检验不成功
    '''
    @ddt.data(
        ['18771917218', 'laobalaoma7272', 'login_success'],
        ['18771917218', 'laobalaoma7272', 'login_success']
    )
    '''
    @ddt.data(*data)
    def test_login_case(self, data):
        user_name, user_pass, assert_text = data
        result = self.login.register_function(user_name, user_pass, assert_text)
        if result:
            self.assertTrue(result, '执行成功1')
        else:
            self.assertFalse(result, '执行失败1')


'''
容器:规定启动哪些测试case
suite = unittest.TestSuite()
    suite.addTest(FirstCase('test_login_success'))
    unittest.TextTestRunner().run(suite)
'''
if __name__ == '__main__':
    case_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    case_path = os.path.join(case_path, 'report', 'first_case.html')
    f = open(case_path, 'wb+')
    suite = unittest.TestLoader().loadTestsFromTestCase(FirstCase)
    runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='This is first', description='第一次测试报告')
    runner.run(suite)

