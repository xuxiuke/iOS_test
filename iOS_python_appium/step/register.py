#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Created on 2019年03月04日

@author: Duke    注册+忘记密码，大部分用例无法翻译
"""

from appiumframework.PO import base_page
from appiumframework.PO import excel
import time
from operator import eq

class Register(base_page.Action):

    # 1、进入注册页
    def click_the_register(self):
        self.find_name('我的').click()  # 点击我的按钮
        self.log_out()  # 如果已经登录，就退出，如果未登录，则不处理
        time.sleep(1)
        self.find_name('注册').click()  # 点击注册按钮
        return self.find_name('输入手机号码')  # 验证页面是否有text输入手机号码

    # 2、手机号格式不正确，下一步按钮不可点击
    def incorrect_format(self):
        self.click_the_register()  # 进入注册页面
        self.find_xpath(excel.xpath_con('registration_page_number')).send_keys('1801398638')  # 输入错误手机号，少于11位
        return self.find_name('下一步') .is_enabled() # 下一步按钮不可点击

    # 3、手机号已被注册-手机号已被注册
    def account_is_registered(self):
        self.click_the_register()  # 进入注册页面
        self.find_xpath(excel.xpath_con('registration_page_number')).send_keys('18013986382')  # 输入已注册手机号
        self.find_name('下一步').click()  # 点击下一步按钮
        time.sleep(2)
        return self.find_name('手机号已被注册')  # 验证是否弹出手机号已被注册弹窗

    # 4、手机号码为空下一步按钮不可点击
    def next_step_not_clickable(self):
        self.click_the_register()  # 进入注册页面
        self.find_xpath(excel.xpath_con('registration_page_number')).send_keys('')  # 不输入
        return self.find_name('下一步').is_enabled()  # 下一步按钮不可点击

    # 5、《使用条款与免责协议》
    def disclaimer_agreement(self):
        self.click_the_register()  # 进入注册页面
        self.find_name('《使用条款与免责协议》').click()  # 点击使用条款和免责协议
        time.sleep(2)
        return self.find_name('南京物联传感技术有限公司')  # 验证页面是否有text南京物联传感技术有限公司

    # 6、《使用条款与免责协议》页面返回注册页面
    def return_register(self):
        self.disclaimer_agreement()  # 《使用条款与免责协议》页面
        self.driver.back()  # 返回上一页
        return self.find_name('输入手机号码')  # 验证页面是否有text输入手机号码

    # 7、进入忘记密码页面
    def forget_the_password(self):
        self.find_name('我的').click()  # 点击我的按钮
        self.log_out()  # 如果已经登录，就退出，如果未登录，则不处理
        self.find_name('忘记密码').click()  # 点击忘记密码按钮
        return self.find_name('输入手机号或邮箱')  # 验证页面是否有text输入手机号或邮箱

    # 8、忘记密码，手机号格式不正确
    def password_incorrect_format(self):
        self.forget_the_password()  # 进入忘记密码页面
        self.find_xpath(excel.xpath_con('forget_password_number')).send_keys('123456')  # 输入错误手机号或者邮箱
        self.find_name('下一步').click()  # 点击下一步按钮
        return self.find_name('请输入正确的邮箱或手机号')  # 验证toast是否正确

    # 9、未输入手机号，下一步按钮不可点击
    def password_not_clickable(self):
        self.forget_the_password()  # 进入忘记密码页面
        self.find_xpath(excel.xpath_con('forget_password_number')).send_keys('')  # 不输入
        return self.find_name('下一步').is_enabled()  # 验证下一步是否可以点击

    # 10、点击忘记密码页面左上X按钮,返回登录页面
    def forget_password_X(self):
        self.forget_the_password()  # 进入忘记密码页面
        self.find_xpath(excel.xpath_con('forget_password_X')).click()  # 点击左上X按钮
        return self.find_xpath(excel.xpath_con('Sign in'))  # 验证是否有登录按钮

    # 11、新密码设置成功,返回登陆页面
    def new_password(self):
        self.forget_the_password()  # 进入忘记密码页面
        self.find_xpath(excel.xpath_con('forget_password_number')).send_keys('18013986382')  # 输入已注册手机号
        self.find_name('下一步').click()  # 点击下一步按钮
        time.sleep(1)
        self.find_name('confirmCode').send_keys('1')
        self.find_name('confirmCode').send_keys('2')
        self.find_name('confirmCode').send_keys('3')
        self.find_name('confirmCode').send_keys('4')
        self.find_name('confirmCode').send_keys('5')
        self.find_name('confirmCode').send_keys('6')
        time.sleep(1)
        self.find_xpath(excel.xpath_con('new_password_number')).send_keys('wl123456789')  # 输入新密码
        self.find_name('完成').click()  # 点击完成按钮
        time.sleep(1)
        text = self.get_text(excel.xpath_con('Login/Register'))  # 获取登录/注册text
        print(text)
        if eq(text, '登录/注册') == 0:  # 验证用户名
            return True
        else:
            return False

    # 12、错误的验证码
    def error_validation_code(self):
        self.forget_the_password()  # 进入忘记密码页面
        self.find_xpath(excel.xpath_con('forget_password_number')).send_keys('18013986382')  # 输入已注册手机号
        self.find_name('下一步').click()  # 点击下一步按钮
        time.sleep(3)
        self.find_name('confirmCode').send_keys('1')
        self.find_name('confirmCode').send_keys('2')
        self.find_name('confirmCode').send_keys('3')
        self.find_name('confirmCode').send_keys('4')
        self.find_name('confirmCode').send_keys('5')
        self.find_name('confirmCode').send_keys('7')
        time.sleep(1)
        return self.find_name('验证码不正确，请重新输入')

    # 13、新密码不足6位
    def password_less_6(self):
        self.forget_the_password()  # 进入忘记密码页面
        self.find_xpath(excel.xpath_con('forget_password_number')).send_keys('18013986382')  # 输入已注册手机号
        self.find_name('下一步').click()  # 点击下一步按钮
        time.sleep(1)
        self.find_name('confirmCode').send_keys('1')
        self.find_name('confirmCode').send_keys('2')
        self.find_name('confirmCode').send_keys('3')
        self.find_name('confirmCode').send_keys('4')
        self.find_name('confirmCode').send_keys('5')
        self.find_name('confirmCode').send_keys('6')
        time.sleep(1)
        self.find_xpath(excel.xpath_con('new_password_number')).send_keys('wl123')  # 输入小于6位新密码
        return self.find_name('完成').is_enabled()  # 验证完成按钮是否可点击
