#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/19 0019 14:58
# @Author  : Aries
# @Site    : 
# @File    : actionMethod.py
# @Software: PyCharm
from selenium import webdriver
from base.find_element import FindElement
import time


class ActionMethod:

    # 打开浏览器
    def open_browser(self, browser):
        if browser == 'chrome':
            self.driver = webdriver.Chrome()
        elif browser == 'firefox':
            self.driver = webdriver.Firefox()
        else:
            self.driver = webdriver.Edge()
        self.driver.maximize_window()

    # 输入地址
    def get_url(self, url):
        self.driver.get(url)

    # 定位元素
    def get_element(self, key):
        fine_element = FindElement(self.driver)
        element = fine_element.get_element(key)
        return element

    # 输入元素
    def send_value(self, value, key):
        element = self.get_element(key)
        element.send_keys(value)

    # 点击元素
    def click_element(self, key):
        self.get_element(key).click()

    # 等待时间
    @staticmethod
    def sleep_time():
        time.sleep(3)

    # 关闭浏览器
    def close_browser(self):
        self.driver.close()

    # 得到title
    def get_title(self):
        return self.driver.title
