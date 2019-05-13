#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Created on 2019年02月21日

@author: Duke    登陆流程
"""

from appiumframework.PO import base_page
from appiumframework.PO import excel
import time

class Login(base_page.Action):
    # 1、登录成功
    def login_success(self):
        self.find_name('我的').click()  # 点击我的按钮
        self.log_out()  # 如果已经登录，则退出账号
        time.sleep(2)
        self.find_ios_predicate("type == 'XCUIElementTypeTextField'").clear()  # 清空输入框
        self.find_ios_predicate("type == 'XCUIElementTypeTextField'").send_keys('18013986382')  # 输入账号
        self.find_ios_predicate("type == 'XCUIElementTypeSecureTextField'").send_keys('wl123456789')  # 输入密码
        self.find_name('登录').click()  # 点击登录
        return self.page_xpath(excel.xpath_con('mine'))  # 验证我的按钮xpath元素存在

    # 2、账号为空
    def none_user(self):
        self.find_name('我的').click()  # 点击我的按钮
        self.log_out()  # 如果已经登录，则退出账号
        self.find_ios_predicate("type == 'XCUIElementTypeTextField'").clear()  # 清空输入框
        self.find_ios_predicate("type == 'XCUIElementTypeSecureTextField'").send_keys('wl123456789')  # 输入密码
        self.find_name('登录').click()  # 点击登录
        if self.find_xpath(excel.xpath_con('Sign in')).is_enabled():
            return False
        else:
            return True

    # 3、密码为空
    def none_password(self):
        self.find_name('我的').click()  # 点击我的按钮
        self.log_out()  # 如果已经登录，则退出账号
        self.find_ios_predicate("type == 'XCUIElementTypeTextField'").clear()  # 清空输入框
        self.find_ios_predicate("type == 'XCUIElementTypeTextField'").send_keys('18013986382')  # 输入账号
        if self.find_xpath(excel.xpath_con('Sign in')).is_enabled():
            return False
        else:
            return True

    # 4、错误的账号
    def wrong_user(self):
        self.find_name('我的').click()  # 点击我的按钮
        self.log_out()  # 如果已经登录，则退出账号
        self.find_ios_predicate("type == 'XCUIElementTypeTextField'").clear()  # 清空输入框
        self.find_ios_predicate("type == 'XCUIElementTypeTextField'").send_keys('180139863')  # 输入账号
        self.find_ios_predicate("type == 'XCUIElementTypeSecureTextField'").send_keys('wl123456789')  # 输入密码
        self.find_name('登录').click()  # 点击登录
        return self.find_name('请输入正确的邮箱或手机号')

    # 5、错误的密码
    def wrong_password(self):
        self.find_name('我的').click()  # 点击我的按钮
        self.log_out()  # 如果已经登录，则退出账号
        self.find_ios_predicate("type == 'XCUIElementTypeTextField'").clear()  # 清空输入框
        self.find_ios_predicate("type == 'XCUIElementTypeTextField'").send_keys('17751027576')  # 输入账号
        self.find_ios_predicate("type == 'XCUIElementTypeSecureTextField'").send_keys('wl12345')  # 输入密码
        self.find_name('登录').click()  # 点击登录
        self.find_name('登录...')  # 验证是否有用户密码错误toast前过渡步骤
        return self.find_name('用户密码错误')

    # 6、连续3次密码错误，取消弹窗
    def wrong_password_3(self):
        self.find_name('我的').click()  # 点击我的按钮
        self.log_out()  # 如果已经登录，则退出账号
        self.find_ios_predicate("type == 'XCUIElementTypeTextField'").clear()  # 清空输入框
        self.find_ios_predicate("type == 'XCUIElementTypeTextField'").send_keys('18952017551')  # 输入账号
        self.find_ios_predicate("type == 'XCUIElementTypeSecureTextField'").send_keys('wl123456')  # 输入密码
        self.find_name('登录').click()  # 点击登录
        self.find_name('登录').click()  # 点击登录
        self.find_name('登录').click()  # 点击登录
        time.sleep(2)
        if self.find_name('取消'):
            pass
        else:
            self.find_name('登录').click()  # 点击登录
            time.sleep(2)
        self.find_name('取消').click()  # 点击弹窗取消按钮
        return self.find_name('取消')

    # 7、连续3次密码错误，找回密码
    def wrong_password_3_findp(self):
        self.find_name('我的').click()  # 点击我的按钮
        self.log_out()  # 如果已经登录，则退出账号
        self.find_ios_predicate("type == 'XCUIElementTypeTextField'").clear()  # 清空输入框
        self.find_ios_predicate("type == 'XCUIElementTypeTextField'").send_keys('18013986382')  # 输入账号
        self.find_ios_predicate("type == 'XCUIElementTypeSecureTextField'").send_keys('wl1234567')  # 输入密码
        self.find_name('登录').click()  # 点击登录
        self.find_name('登录').click()  # 点击登录
        self.find_name('登录').click()  # 点击登录
        time.sleep(2)
        if self.find_name('取消'):
            pass
        else:
            self.find_name('登录').click()  # 点击登录
            time.sleep(2)
        self.find_xpath(excel.xpath_con('Retrieve password')).click()  # 点击弹窗找回密码按钮
        return self.find_name('输入手机号或邮箱')
        