#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Created on 2019年03月04日

@author: Duke    游客模式
"""

from appiumframework.PO import base_page
from appiumframework.PO import excel

class Tourist(base_page.Action):

    # 1、以游客模式登录首页
    def home_page(self):
        self.find_name('我的').click()  # 点击我的按钮
        self.log_out()  # 如果已经登录，则退出账号
        self.find_xpath(excel.xpath_con('login_page_X')).click()  # 点击关闭登录页面
        self.find_name('首页').click()  # 点击首页按钮
        if self.find_name('离家') and self.find_name('睡觉') and self.find_name('起床') and self.find_name('就餐'):  # 随机查找4个默认的场景名称
            return '找到默认场景'
        else:
            return '未找到默认场景'

    # 2、以游客模式点击消息中心
    def base_img_right(self):
        self.home_page()  # 游客模式首页
        self.find_name('home message icon').click()  # 点击小铃铛
        return self.find_xpath(excel.xpath_con('Sign in'))  # 验证登录页面是否有登录按钮xpath

    # 3、以游客模式点击场景
    def click_the_scene(self):
        self.home_page()  # 游客模式首页
        self.find_name('离家').click()  # 点击离家场景
        return self.find_xpath(excel.xpath_con('Sign in'))  # 验证登录页面是否有登录按钮xpath

    # 4、以游客模式点击【设备】
    def click_the_device(self):
        self.find_name('我的').click()  # 点击我的按钮
        self.log_out()  # 如果已经登录，则退出账号
        self.find_xpath(excel.xpath_con('login_page_X')).click()  # 点击关闭登录页面
        self.find_name('设备').click()  # 点击设备按钮
        return self.find_xpath(excel.xpath_con('Sign in'))  # 验证登录页面是否有登录按钮xpath

    # 5、以游客模式点击【我的】
    def click_the_mine(self):
        self.find_name('我的').click()  # 点击我的按钮
        self.log_out()  # 如果已经登录，则退出账号
        self.find_xpath(excel.xpath_con('login_page_X')).click()  # 点击关闭登录页面
        self.find_name('我的').click()  # 点击我的按钮
        return self.find_name('物联会员')

    # 6、以游客模式点击【登录/注册】
    def click_the_land(self):
        self.find_name('我的').click()  # 点击我的按钮
        self.log_out()  # 如果已经登录，则退出账号
        return self.find_xpath(excel.xpath_con('Sign in'))  # 验证登录页面是否有登录按钮xpath

    # 7、以游客模式点击【网关中心】
    def click_the_gateway_center(self):
        self.find_name('我的').click()  # 点击我的按钮
        self.log_out()  # 如果已经登录，则退出账号
        self.find_xpath(excel.xpath_con('login_page_X')).click()  # 点击关闭登录页面
        self.find_name('网关中心').click()  # 点击网关中心按钮
        return self.find_xpath(excel.xpath_con('Sign in'))  # 验证登录页面是否有登录按钮xpath

    # 8、以游客模式点击【在线客服】
    def click_the_customer_service(self):
        self.find_name('我的').click()  # 点击我的按钮
        self.log_out()  # 如果已经登录，则退出账号
        self.find_xpath(excel.xpath_con('login_page_X')).click()  # 点击关闭登录页面
        self.find_name('在线客服').click()  # 点击在线客服按钮
        return self.find_xpath(excel.xpath_con('Sign in'))  # 验证登录页面是否有登录按钮xpath

    # 9、以游客模式点击【智能】
    def click_the_smart(self):
        self.home_page()  # 游客模式首页
        self.find_name('智能').click()  # 点击智能
        return self.find_xpath(excel.xpath_con('Sign in'))  # 验证登录页面是否有登录按钮xpath

    # 10、以游客模式点击【设置】
    def click_the_setting(self):
        self.find_name('我的').click()  # 点击我的按钮
        self.log_out()  # 如果已经登录，则退出账号
        self.find_xpath(excel.xpath_con('login_page_X')).click()  # 点击关闭登录页面
        self.find_name('设置').click()  # 点击设置按钮
        return self.find_xpath(excel.xpath_con('Sign in'))  # 验证登录页面是否有登录按钮xpath

    # 11、以游客模式点击【分享管理】
    def click_the_sharing_management(self):
        self.find_name('我的').click()  # 点击我的按钮
        self.log_out()  # 如果已经登录，则退出账号
        self.find_xpath(excel.xpath_con('login_page_X')).click()  # 点击关闭登录页面
        self.find_name('分享管理').click()  # 点击分享管理按钮
        return self.find_xpath(excel.xpath_con('Sign in'))  # 验证登录页面是否有登录按钮xpath

    # 12、以游客模式点击【物联会员】
    def click_the_wulian_member(self):
        self.find_name('我的').click()  # 点击我的按钮
        self.log_out()  # 如果已经登录，则退出账号
        self.find_xpath(excel.xpath_con('login_page_X')).click()  # 点击关闭登录页面
        self.find_name('物联会员').click()  # 点击物联会员按钮
        return self.find_xpath(excel.xpath_con('Sign in'))  # 验证登录页面是否有登录按钮xpath

    # 13、以游客模式点击【意见反馈】
    def click_the_feedback(self):
        self.find_name('我的').click()  # 点击我的按钮
        self.log_out()  # 如果已经登录，则退出账号
        self.find_xpath(excel.xpath_con('login_page_X')).click()  # 点击关闭登录页面
        self.find_name('意见反馈').click()  # 点击意见反馈按钮
        return self.find_xpath(excel.xpath_con('Sign in'))  # 验证登录页面是否有登录按钮xpath

    # 14、以游客模式点击【关于】
    def click_the_about(self):
        self.find_name('我的').click()  # 点击我的按钮
        self.log_out()  # 如果已经登录，则退出账号
        self.find_xpath(excel.xpath_con('login_page_X')).click()  # 点击关闭登录页面
        self.find_name('关于').click()  # 点击关于按钮
        return self.find_name('关于物联')  # 验证页面是否有关于物联name或者lebel
