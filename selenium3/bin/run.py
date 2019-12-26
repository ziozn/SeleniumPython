#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/12 0012 11:02
# @Author  : Aries
# @Site    : 
# @File    : run.py
# @Software: PyCharm
import unittest
import os


class RunCase:
    def __init__(self):
        case_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        case_path = os.path.join(case_path, 'case')
        suite = unittest.defaultTestLoader.discover(case_path, 'unittest_*.py')
        unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    RunCase()
