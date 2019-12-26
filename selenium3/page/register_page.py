#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/11 0011 9:48
# @Author  : Aries
# @Site    : 
# @File    : register_page.py
# @Software: PyCharm
from base.find_element import FindElement


# 输入配置信息
class RegisterPage:
    def __init__(self, driver):
        self.fd = FindElement(driver)

    # 获取用户名
    def get_user_name_element(self):
        return self.fd.get_element('user_name')

    # 获取密码
    def get_user_pass_element(self):
        return self.fd.get_element('user_pass')

    # 获取跳转到登录界面的按钮
    def get_pass_element(self):
        return self.fd.get_element('pass')

    # 获取登录按钮
    def get_login_element(self):
        return self.fd.get_element('login')

    # 获取登陆失败的提示信息
    def get_login_error_element(self):
        return self.fd.get_element('login_error')

    # 获取登陆成功的提示信息
    def get_login_success_element(self):
        return self.fd.get_element('login_success')
