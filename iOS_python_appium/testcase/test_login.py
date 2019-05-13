#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Created on 2019年02月21日

@author: Duke    登陆测试    7条用例
"""

from appiumframework.PO.open_app import Open_app
from appiumframework.step import login
import unittest
import warnings

class Test001(unittest.TestCase, login.Login): # TestCase类，所有测试用例类继承的基本类
    """登陆测试"""
    # setUp()方法用于测试用例执行前的初始化工作，如打开APP
    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)  # 屏蔽ResourceWarning报警
        self.ina = Open_app(self)
        self.ina.open()
        self.driver = self.ina.get_driver()
        self.verificationErrors = []  # 错误信息打印到这个列表
        self.accept_next_alert = True  # 是否继续接受下个警告

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

    # 1、登陆成功
    def test_login_success(self):
        self.assertTrue(self.login_success())

    # 2、账号为空
    def test_none_user(self):
        self.assertTrue(self.none_user())

    # 3、密码为空
    def test_none_password(self):
        self.assertTrue(self.none_password())

    # 4、错误的账号（toast：账号或密码不正确）
    def test_wrong_user(self):
        self.assertTrue(self.wrong_user())

    # 5、错误的密码（toast：用户密码错误）
    def test_wrong_password(self):
        self.assertTrue(self.wrong_password())

    # 6、连续3次密码错误，取消弹窗
    def test_wrong_password_3(self):
        self.assertFalse(self.wrong_password_3())

    # 7、连续3次密码错误，找回密码
    def test_wrong_password_3_findp(self):
        self.assertTrue(self.wrong_password_3_findp())
