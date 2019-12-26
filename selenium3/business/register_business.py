#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/11 0011 9:35
# @Author  : Aries
# @Site    : 
# @File    : register_business.py
# @Software: PyCharm
from handle.register_handle import RegisterHandle


# 执行操作
class RegisterBusiness:

    def __init__(self, driver):
        self.register_h = RegisterHandle(driver)

    def user_base(self, name, pwd):
        self.register_h.jump_login()
        self.register_h.send_user_name(name)
        self.register_h.send_user_pass(pwd)
        self.register_h.click_register_button()

    # 执行操作
    def login(self, name, pwd):
        self.user_base(name, pwd)
        if self.register_h.obtain_error_tips('login_error') is None:
            print('账号密码输入正确')
            return True
        else:
            print('账号密码输入错误')
            return False

    def register_function(self, user_name, user_pass, assert_text):
        self.user_base(user_name, user_pass)
        if self.register_h.obtain_error_tips(assert_text) is None:
            print('账号密码输入正确')
            return True
        else:
            print('账号密码输入错误')
            return False

    # 执行操作
    def login_user_name(self, name, pwd):
        self.user_base(name, pwd)
        if self.register_h.obtain_error_tips('login_user_name_error') is None:
            print('账号检验成功')
        else:
            print('账号检验不成功')
