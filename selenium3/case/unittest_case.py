#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/10 0010 17:47
# @Author  : Aries
# @Site    : 
# @File    : unittest_case.py
# @Software: PyCharm
from business.register_business import RegisterBusiness
from selenium import webdriver
import time
import unittest
import os
import HTMLTestRunner


# 这里可以验证各种case，比如账号长度不合格，密码长度不合格。目前所用的只是两条较为简单的登陆成功以及失败的case
class FirstCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('所有case执行之前的前置')

    @classmethod
    def tearDownClass(cls):
        print('所有case执行之后的后置')

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://login.taobao.com/member/login.jhtml?redirectURL=https%3A%2F%2Fuland.taobao.com%2Fsem%'
                   '2Ftbsearch%3Frefpid%3Dmm_26632258_3504122_32538762%26keyword%3D%25E5%25A5%25B3%25E8%25A3%2585'
                   '%26clk1%3Dba89c9a0842524f3beb1c264b8e3a993%26upsid%3Dba89c9a0842524f3beb1c264b8e3a993')
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
    def test_login_pass_error(self):
        result = self.login.login('18771917218', 'laobalaoma7272')
        print(self.assertTrue(result, '执行成功1'))
        # self.assertFalse(result, '执行失败1')

    # 账号密码输入正确
    def test_login_success(self):
        result = self.login.login('18771917218', 'laobalaoma7272')
        self.assertTrue(result, '执行成功2')
        # self.assertFalse(result, '执行失败2')


'''
容器:规定启动哪些测试case
suite = unittest.TestSuite()
    suite.addTest(FirstCase('test_login_success'))
    unittest.TextTestRunner().run(suite)
'''
if __name__ == '__main__':
    # unittest.main()
    case_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    case_path = os.path.join(case_path, 'report', 'first_case.html')
    print(case_path)
    f = open(case_path, 'wb')
    suite = unittest.TestSuite()
    suite.addTest(FirstCase('test_login_success'))
    suite.addTest(FirstCase('test_login_user_error'))
    suite.addTest(FirstCase('test_login_pass_error'))
    # unittest.TextTestRunner().run(suite)
    runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='This is first', description='第一次测试报告')
    runner.run(suite)
