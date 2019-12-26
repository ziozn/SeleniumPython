#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/10 0010 17:48
# @Author  : Aries
# @Site    : 
# @File    : register_handle.py
# @Software: PyCharm
from page.register_page import RegisterPage


# 针对定位信息进行内容输入操作
class RegisterHandle:

    def __init__(self, driver):
        self.register_p = RegisterPage(driver)

    # 跳转到登录界面
    def jump_login(self):
        self.register_p.get_pass_element().click()

    # 输入用户名
    def send_user_name(self, name):
        self.register_p.get_user_name_element().send_keys(name)

    # 输入密码
    def send_user_pass(self, pwd):
        self.register_p.get_user_pass_element().send_keys(pwd)

    # 点击登录
    def click_register_button(self):
        self.register_p.get_login_element().click()

    # 获取错误提示
    def obtain_error_tips(self, info):
        if info == 'login_success':
            test = self.register_p.get_login_success_element().text
        elif info == 'login_error':
            test = self.register_p.get_login_error_element().text
        return test

